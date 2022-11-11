"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class TopActivityReply(BaseModel):
    """"""

    online: Optional["TopOnline"] = None
    """当前生效的资源"""
    hash: builtins.str
    """对online内容进行hash和上次结果一样则不重新加载"""


class TopOnline(BaseModel):
    """当前生效的资源"""

    type: builtins.int
    """活动类型
    1:七日活动 2:后台配置
    """
    icon: builtins.str
    """图标"""
    uri: builtins.str
    """跳转链接"""
    unique_id: builtins.str
    """资源状态标识(后台配置)"""
    animate: Optional["Animate"] = None
    """动画资源"""
    red_dot: Optional["RedDot"] = None
    """红点"""
    name: builtins.str
    """活动名称"""
    interval: builtins.int
    """轮询间隔 单位秒"""


class Animate(BaseModel):
    """动画资源"""

    icon: builtins.str
    """动效结束展示icon"""
    json: builtins.str
    """7日活动动画"""
    svg: builtins.str
    """s10活动svg动画"""
    loop: builtins.int
    """循环次数(默认0不返回 表示无限循环)"""


class RedDot(BaseModel):
    """红点"""

    type: builtins.int
    """红点类型
    1:纯红点 2:数字红点
    """
    number: builtins.int
    """如果是数字红点 显示的数字"""


TopActivityReply.update_forward_refs()
TopOnline.update_forward_refs()
Animate.update_forward_refs()
RedDot.update_forward_refs()