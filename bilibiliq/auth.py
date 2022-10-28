import time
import base64
from hashlib import md5
from dataclasses import dataclass
from urllib.parse import urlencode
from typing import Any, Dict, Tuple, Union, Literal, Optional

import rsa

from .typing import StrDict
from .request import request_passport
from .exception import (
    RESTError,
    NeedVerify,
    NotScanQRCode,
    QRCodeExpired,
    QRCodeNotAccepted,
)

APP_KEY = "4409e2ce8ffd12b8"
APP_SECRET = "59b43e04ad6965f34319062b478f83dd"


@dataclass
class Auth:
    DedeUserID: Optional[str] = None
    DedeUserID__ckMd5: Optional[str] = None
    SESSDATA: Optional[str] = None
    bili_jct: Optional[str] = None
    sid: Optional[str] = None
    refresh_token: Optional[str] = None
    access_token: Optional[str] = None


async def get_captcha() -> StrDict:
    """
    申请 Captcha 验证码

    返回：
        一个 dict

        token (str) 登录 API token
        gt (str) 极验 ID
        challenge (str) 极验 KEY

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/tree/master/login/login_action#%E7%94%B3%E8%AF%B7captcha%E9%AA%8C%E8%AF%81%E7%A0%81
    """
    data, _ = await request_passport(
        "x/passport-login/captcha", "GET", params={"source": "main_web"}
    )
    return {
        "token": data["token"],
        "gt": data["geetest"]["gt"],
        "challenge": data["geetest"]["challenge"],
    }


async def get_hash_and_key() -> Tuple[str, str]:
    """
    获取公钥和盐

    返回：
        一个 tuple (hash, key)

        hash (str) 密码盐值 有效时间为 20s，需要拼接在明文密码之前
        key (str) rsa 公钥 PEM 格式编码

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/password.md#%E8%8E%B7%E5%8F%96%E5%85%AC%E9%92%A5%E7%9B%90web%E7%AB%AF
    """
    data, _ = await request_passport(
        "x/passport-login/web/key", "GET", params={"source": "main_web"}
    )
    return data["hash"], data["key"]


def _encrypt_data(key: str, text: str) -> str:
    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(key.encode())
    crypto = rsa.encrypt(text.encode("utf-8"), public_key)
    return base64.b64encode(crypto).decode("utf-8")


async def web_login(
    username: str,
    password: str,
    token: str,
    challenge: str,
    validate: str,
    seccode: Optional[str] = None,
) -> Auth:
    """
    Web 登录操作

    参数：
        username (str) 用户登录账号 手机号或邮箱地址
        password (str) 密码（无需加盐）
        token (str) 登录 API token
        challenge (str) 极验 KEY
        validate (str) 极验 validate
        seccode (Optional[str]) 极验 seccode，可不提供，不提供将根据 validate 计算

    返回：
        Auth 对象

    异常：
        NeedVerify 当需要验证手机号时引发
        出现此种情况请使用 `sms_login` 登录

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/password.md#%E7%99%BB%E5%BD%95%E6%93%8D%E4%BD%9Cweb%E7%AB%AF
    """
    if not seccode:
        seccode = f"{validate}|jordan"

    salt, key = await get_hash_and_key()

    password = _encrypt_data(key, salt + password)

    data, cookie = await request_passport(
        "x/passport-login/web/login",
        "POST",
        data={
            "username": username,
            "password": password,
            "keep": 0,
            "token": token,
            "challenge": challenge,
            "validate": validate,
            "seccode": seccode,
        },
    )
    if data["status"] == 2:
        # 本次登录环境存在风险, 需使用手机号进行验证或绑定
        raise NeedVerify
    cookie_ = {k: v.value for k, v in cookie.items()}
    return Auth(refresh_token=data["refresh_token"], **cookie_)


async def web_send_sms_code(
    cid: int,
    tel: int,
    token: str,
    challenge: str,
    validate: str,
    seccode: Optional[str] = None,
) -> str:
    """
    Web 发送短信验证码

    参数：
        cid (int) 国际冠字码，可从 `get_country_list` 获取（其中的 `country_id`）
        tel (int) 手机号
        token (str) 登录 API token
        challenge (str) 极验 KEY
        validate (str) 极验 validate
        seccode (Optional[str]) 极验 seccode，可不提供，不提供将根据 validate 计算

    返回：
        captcha_key (str)
        短信登录 token

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/SMS.md#%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81web%E7%AB%AF
    """
    if not seccode:
        seccode = f"{validate}|jordan"
    data, _ = await request_passport(
        "x/passport-login/web/sms/send",
        "POST",
        data={
            "cid": cid,
            "tel": tel,
            "token": token,
            "source": "main_web",
            "challenge": challenge,
            "validate": validate,
            "seccode": seccode,
        },
    )
    return data["captcha_key"]


async def get_country_list() -> Dict[str, Dict[str, Union[str, int]]]:
    """
    获取国际冠字码

    返回：
        一个 dict，键为 cname (str)，值为一个字典

        id (int) ID 可用于发送验证码
        country_id (str) 国际冠字码

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/SMS.md#%E8%8E%B7%E5%8F%96%E5%9B%BD%E9%99%85%E5%86%A0%E5%AD%97%E7%A0%81web%E7%AB%AF
    """
    data, _ = await request_passport("web/generic/country/list", "GET")
    countries: Dict[str, Dict[str, Union[str, int]]] = {}
    for countries_ in data.values():
        for country in countries_:
            countries[country.pop("cname")] = country
    return countries


async def web_sms_login(
    cid: int, tel: int, code: int, captcha_key: str, keep: bool = False
) -> Auth:
    """
    Web 使用短信验证码登录

    参数：
        cid (int) 国际冠字码，可从 `get_country_list` 获取（其中的 `id`）
        tel (int) 手机号
        code (int) 短信验证码
        captcha_key (str) 发送短信验证码时获取的 `captcha_key`
        keep (bool) 是否记住登录（默认为 False）

    返回：
        Auth 对象

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/SMS.md#%E4%BD%BF%E7%94%A8%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81%E7%99%BB%E5%BD%95web%E7%AB%AF
    """
    _, cookie = await request_passport(
        "x/passport-login/web/login/sms",
        "POST",
        data={
            "cid": cid,
            "tel": tel,
            "source": "main_web",
            "code": code,
            "captcha_key": captcha_key,
            "keep": keep,
        },
    )
    cookie_ = {k: v.value for k, v in cookie.items()}
    return Auth(**cookie_)


async def generate_qrcode_web() -> Tuple[str, str]:
    """
    申请二维码（web端）

    返回：
        一个 tuple (url, qrcode_key)

        url (str) 登录页面 url（可直接点击验证，也可生成二维码扫描）
        qrcode_key (str) 扫码登录秘钥

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E7%94%B3%E8%AF%B7%E4%BA%8C%E7%BB%B4%E7%A0%81web%E7%AB%AF
    """
    data, _ = await request_passport(
        "x/passport-login/web/qrcode/generate", "GET"
    )
    return data["url"], data["qrcode_key"]


async def qrcode_login_web(qrcode_key: str) -> Auth:
    """
    扫码登录（web端）

    返回：
        Auth 对象

    参数：
        qrcode_key (str) 扫码登录秘钥

    异常：
        QRCodeExpired 二维码已过期
        QRCodeNotAccepted 二维码已扫描，但还未同意登录
        NotScanQRCode 未扫描二维码

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E7%94%B3%E8%AF%B7%E4%BA%8C%E7%BB%B4%E7%A0%81web%E7%AB%AF
    """
    data, cookie = await request_passport(
        "x/passport-login/web/qrcode/poll",
        "GET",
        params={"qrcode_key": qrcode_key},
    )

    if exc := {
        86038: QRCodeExpired,
        86090: QRCodeNotAccepted,
        86101: NotScanQRCode,
    }.get(data["code"]):
        raise exc
    cookie_ = {k: v.value for k, v in cookie.items()}
    return Auth(refresh_token=data["refresh_token"], **cookie_)


def _sign(params: Dict[str, Any]) -> None:
    params["local_id"] = 0
    params["appkey"] = APP_KEY
    params["ts"] = int(time.time())
    params["sign"] = md5(
        f"{urlencode(sorted(params.items()))}{APP_SECRET}".encode("utf-8")
    ).hexdigest()


async def generate_qrcode_tv() -> Tuple[str, str]:
    """
    申请二维码（TV端）

    返回：
        一个 tuple (url, auth_code)

        url (str) 登录页面 url（可直接点击验证，也可生成二维码扫描）
        auth_code (str) 扫码登录秘钥

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E7%94%B3%E8%AF%B7%E4%BA%8C%E7%BB%B4%E7%A0%81tv%E7%AB%AF
    """
    params = {}
    _sign(params)
    data, _ = await request_passport(
        "x/passport-tv-login/qrcode/auth_code", "POST", params=params
    )
    return data["url"], data["auth_code"]


async def qrcode_login_tv(auth_code: str) -> Auth:
    """
    扫码登录（TV端）

    返回：
        Auth 对象

    参数：
        auth_code (str) 扫码登录秘钥

    异常：
        QRCodeExpired 二维码已过期
        QRCodeNotAccepted 二维码已扫描，但还未同意登录
        NotScanQRCode 未扫描二维码

    参考：
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E7%94%B3%E8%AF%B7%E4%BA%8C%E7%BB%B4%E7%A0%81web%E7%AB%AF
    """
    params = {"auth_code": auth_code}
    _sign(params)
    try:
        data, _ = await request_passport(
            "x/passport-tv-login/qrcode/poll",
            "POST",
            params=params,
        )
        return Auth(
            refresh_token=data["token_info"]["refresh_token"],
            access_token=data["token_info"]["access_token"],
        )
    except RESTError as e:
        if e.code == 86039:
            raise QRCodeNotAccepted
        else:
            raise


async def qrcode_terminal_login(type_: Literal["web", "tv"] = "web") -> Auth:
    """
    将登录二维码显示在终端并阻塞，直到登录成功或过期

    返回：
        Auth 对象

    参数：
        type_ (Literal["web", "tv"]) 二维码登录类型（默认为 `web`）

    异常：
        QRCodeExpired 二维码已过期
    """
    try:
        from qrcode import QRCode
    except ImportError:
        raise ImportError(
            (
                "Run `pip install bilibiliq[qrcode]` to enable "
                "`qrcode_terminal_login`"
            )
        ) from None
    if type_ == "web":
        generator = generate_qrcode_web
        login = qrcode_login_web
    else:
        generator = generate_qrcode_tv
        login = qrcode_login_tv

    url, code = await generator()
    qrcode = QRCode()
    qrcode.add_data(url)
    qrcode.print_ascii()

    while True:
        try:
            return await login(code)
        except (NotScanQRCode, QRCodeNotAccepted):
            continue
        except Exception:
            raise
