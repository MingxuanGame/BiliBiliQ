import sys
import asyncio
import argparse
from pathlib import Path
from types import EllipsisType
from typing import Tuple, Union, Literal, Optional

from bilibiliq.rest.user import UserClient
from bilibiliq.exception import RESTError, NeedVerify, QRCodeExpired
from bilibiliq.auth import (
    Auth,
    web_login,
    get_captcha,
    web_sms_login,
    web_send_sms_code,
    qrcode_terminal_login,
)

if sys.platform == "win32":
    # https://github.com/aio-libs/aiohttp/issues/4324
    _loop = asyncio.new_event_loop()
    asyncio.set_event_loop(_loop)
else:
    _loop = asyncio.get_running_loop()

DESC = """
BiliBiliQ 命令行程序，可用于获取或保存鉴权信息，供程序使用
支持短信登录，密码登录，扫码登录（需安装 qrcode 扩展）
允许指定客户端类型为 TV 或 Web（使用 -c 传入，默认为 tv）

短信登录必须传入手机号，可选传入国际区号
  %(prog)s sms <手机号> [国际区号]
  e.g. %(prog)s sms 1xxxxxxxxx0 +86
密码登录必须传入账号（手机号或邮箱），密码
  %(prog)s password <账号> <密码>
  e.g. %(prog)s password 1xxxxxxxxx0 12345678
短信登录和密码登录需要进行 geetest 验证，可前往 https://kuresaru.github.io/geetest-validator
输入提供的 gt 和 challenge 进行验证并将返回的 validate 传入程序

扫码登录需安装 qrcode 扩展，可使用如下命令安装
  pip install bilibiliq[qrcode]  # 使用 pip
  pdm install -G qrcode  # 使用 pdm
扫码登录无需传入参数
  %(prog)s qrcode
使用哔哩哔哩客户端扫描在终端打印的二维码即可，若二维码失效可结束程序再登录

-s 参数用于保存鉴权信息到 json 文件
如果不传入参数，则默认以 <登录账号 UID>.json 的名称保存到用户数据目录
  macOS:     ~/Library/Application Support/BiliBiliQ
  Unix:      ~/.local/share/BiliBiliQ (XDG default)
  Windows:   C:\\Users\\<username>\\AppData\\Local\\BiliBiliQ\\BiliBiliQ
如果传入参数，则以参数为文件名保存文件
保存后的文件可使用 `Auth.load_from_file` 读取
下方为示例及对应的读取代码

  不传入参数：
    %(prog)s -s qrcode
    -----------------------------
    from bilibiliq.auth import Auth

    auth = Auth.load_from_file(uid=<登录账号的UID>)

  传入参数：
    %(prog)s -s ./auth.json qrcode
    -----------------------------------------
    from pathlib import Path

    from bilibiliq.auth import Auth

    auth = Auth.load_from_file(Path("./auth.json"))
"""


async def _geetest() -> Tuple[str, str, str]:
    captcha = await get_captcha()
    print("请前往 https://kuresaru.github.io/geetest-validator 进行 geetest 验证")
    print(f"gt: {captcha['gt']}")
    print(f"challenge: {captcha['challenge']}")
    validate = input("validate >>> ")
    return captcha['challenge'], validate, captcha["token"]


def _print_auth(auth: Auth) -> None:
    auth_ = auth.dict(exclude_none=True)
    for k, v in auth_.items():
        print(f"{k}: {v}")


async def sms(phone: int, phone_id: int = +86) -> Auth:
    challenge, validate, token = await _geetest()
    sms_key = await web_send_sms_code(
        phone_id, phone, token, challenge, validate
    )
    print("已发送验证码，请注意查收")
    sms_code = input("验证码 >>> ")
    return await web_sms_login(86, phone, int(sms_code), sms_key, True)


async def password(account: str, password: str) -> Optional[Auth]:
    challenge, validate, token = await _geetest()
    try:
        return await web_login(account, password, token, challenge, validate)
    except NeedVerify:
        print("fatal: 本次登录环境存在风险, 需使用手机号进行验证或绑定")
        print("请使用其他方式登录")


async def qrcode(type_: Literal["tv", "web"] = "tv") -> Optional[Auth]:
    print("\n请使用哔哩哔哩客户端扫描下方二维码")
    try:
        return await qrcode_terminal_login(type_)
    except RuntimeError:
        print("fatal: 未安装 qrcode 扩展")
        print("pip install bilibiliq[qrcode]")
        print("pdm install -G qrcode")
    except QRCodeExpired:
        print("fatal: 二维码已过期")


def _login(namespace: argparse.Namespace) -> Optional[Auth]:
    if namespace.type == "sms":
        func = sms(namespace.phone, namespace.phone_id)
    elif namespace.type == "password":
        func = password(namespace.account, namespace.password)
    else:
        func = qrcode(namespace.client_type)
    try:
        return _loop.run_until_complete(func)
    except RESTError as e:
        print(f"bilibili: {e.message} (code: {e.code})")
    except Exception:
        return


async def _print_user_name(auth: Auth) -> int:
    async with UserClient(auth) as client:
        info = await client.get_self_info()
        print(f"{info.name}（UID：{info.mid}）登录成功！")
        return info.mid


def _save_auth(auth: Auth, uid: int, file: Union[str, EllipsisType]) -> None:
    try:
        if isinstance(file, EllipsisType):
            print(
                f"已保存鉴权信息到 {auth.save_to_file(uid=uid)}，"
                f"可使用 `Auth.load_from_file(uid={uid})` 读取"
            )
        else:
            path = Path(file)
            print(
                f"已保存鉴权信息到 {auth.save_to_file(path)}，"
                "可使用 `Auth.load_from_file"
                f'(pathlib.Path(r"{path.resolve()}"))` 读取'
            )
    except OSError:
        print("fatal: 保存文件时出错")
        raise


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bilibiliq-auth",
        description=DESC,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-c",
        "--client-type",
        help="客户端类型：TV端（返回可用于 gRPC 请求），Web端",
        choices=["tv", "web"],
        default="tv",
        type=str,
    )

    parser.add_argument(
        "-s", "--save-file", nargs="?", type=str, const=..., help="保存鉴权信息"
    )
    subparsers = parser.add_subparsers(help="登录方式", dest="type")

    sms_parser = subparsers.add_parser("sms", help="短信登录")
    sms_parser.add_argument("phone", type=int, help="手机号")
    sms_parser.add_argument(
        "--phone-id", type=int, help="手机区号（默认为+86）", default=+86
    )
    password_parser = subparsers.add_parser("password", help="密码登录")
    password_parser.add_argument("account", type=str, help="手机号或邮箱地址")
    password_parser.add_argument("password", type=str, help="密码")
    qrcode_parser = subparsers.add_parser("qrcode", help="密码登录")  # noqa: F841

    namespace = parser.parse_args()
    if namespace.type is None:
        parser.print_help()
        parser.exit(1)

    auth = _login(namespace)
    if not auth:
        parser.exit(1)
    uid = _loop.run_until_complete(_print_user_name(auth))
    print()
    if save_file := namespace.save_file:
        _save_auth(auth, uid, save_file)
    else:
        _print_auth(auth)

    parser.exit()


if __name__ == "__main__":
    main()
