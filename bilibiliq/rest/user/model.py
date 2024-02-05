import datetime
from typing import Literal, Optional

from pydantic import HttpUrl, BaseModel, validator


class Label(BaseModel):
    """大会员标签"""

    text: Literal[
        "大会员", "年度大会员", "十年大会员", "百年大会员", "最强绿鲤鱼", ""
    ]
    """会员类型文案"""
    label_theme: Literal[
        "vip",
        "annual_vip",
        "ten_annual_vip",
        "hundred_annual_vip",
        "fools_day_hundred_annual_vip",
        "",
    ]
    """
    会员标签
    vip：大会员
    annual_vip：年度大会员
    ten_annual_vip：十年大会员
    hundred_annual_vip：百年大会员
    fools_day_hundred_annual_vip：最强绿鲤鱼
    """
    text_color: str
    """会员标签"""
    bg_color: str
    """会员标签背景颜色，一般为 #FB7299"""
    img_label_uri_hans: str
    """大会员牌子动图（简体版）"""
    img_label_uri_hans_static: HttpUrl
    """大会员牌子图片（简体版）"""
    img_label_uri_hant_static: HttpUrl
    """大会员牌子图片（繁体版）"""


class Vip(BaseModel):
    """大会员信息"""

    type: Literal[0, 1, 2]
    """
    会员类型
    0：无
    1：月大会员
    2：年度及以上大会员
    """
    status: bool
    """会员状态"""
    due_date: datetime.datetime
    """会员过期时间"""
    vip_pay_type: bool
    """
    支付类型
    0：未支付（常见于官方账号）
    1：已支付（以正常渠道获取的大会员均为此值）
    """
    label: Label
    """会员标签"""
    avatar_subscript: bool
    """是否显示会员图标"""
    nickname_color: str
    """会员昵称颜色，一般为 #FB7299"""
    role: Optional[Literal[0, 1, 3, 7, 15]] = None
    """
    大会员角色类型
    0：未开通
    1：月度大会员
    3：年度大会员
    7：十年大会员
    15：百年大会员
    """
    tv_vip_status: Optional[bool] = None
    """电视大会员状态"""
    tv_vip_pay_type: Optional[int] = None
    """电视大会员支付类型"""


class Pendant(BaseModel):
    """头像框"""

    pid: int
    """头像框id"""
    name: str
    """头像框名称"""
    image: str
    """头像框图片url"""
    image_enhance: str
    """头像框图片url"""
    image_enhance_frame: str
    """头像框图片逐帧序列url"""


class Nameplate(BaseModel):
    """勋章"""

    nid: int
    """勋章id"""
    name: str
    """勋章名称"""
    image: str
    """勋章图标"""
    image_small: str
    """勋章图标（小）"""
    level: str
    """勋章等级"""
    condition: str
    """获取条件"""


class Official(BaseModel):
    """账号认证"""

    role: int
    """认证类型"""
    title: str
    """认证信息"""
    desc: str
    """认证备注"""
    type: Literal[-1, 0, 1]
    """
    是否认证
    -1：无
    0：个人认证
    1：机构认证
    """


# class Profession(BaseModel):
#     id: int
#     name: str
#     show_name: str
#     is_show: int
#     category_one: str
#     realname: str
#     title: str
#     department: str


# class Colour(BaseModel):
#     dark: str
#     normal: str


# class Honours(BaseModel):
#     mid: int
#     colour: Colour
#     tags: Any


class LevelExp(BaseModel):
    """等级信息"""

    current_level: Literal[0, 1, 2, 3, 4, 5, 6]
    """当前等级"""
    current_min: int
    """当前等级最低经验"""
    current_exp: int
    """当前经验"""
    next_exp: int
    """升级最低经验"""
    level_up: datetime.datetime
    """升级时间"""


class SelfInfo(BaseModel):
    """自身信息"""

    mid: int
    """用户 UID"""
    name: str
    """用户名"""
    sex: Literal["男", "女", "保密"]
    """性别"""
    face: HttpUrl
    """头像图片 URL"""
    sign: str
    """签名"""
    rank: int
    """目前尚不明确"""
    level: Literal[0, 1, 2, 3, 4, 5, 6]
    """用户等级"""
    moral: int
    """节操"""
    silence: bool
    """封禁状态"""
    email_status: bool
    """已验证邮箱"""
    tel_status: bool
    """已验证手机号"""
    vip: Vip
    """大会员"""
    pendant: Pendant
    """头像框"""
    nameplate: Nameplate
    """勋章"""
    official: Official
    """账号认证"""
    birthday: datetime.date
    """生日"""
    face_nft: bool
    """是否为 nft 头像"""
    is_senior_member: bool
    """是否为硬核会员"""
    level_exp: LevelExp
    """等级信息"""
    coins: float
    """硬币数"""
    following: int
    """粉丝数"""
    follower: int
    """粉丝数"""

    @validator("birthday")
    def name_must_contain_space(cls, v):
        return v + datetime.timedelta(days=1)

    # profession: Profession
    # honours: Honours
