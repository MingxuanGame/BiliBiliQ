# BiliBiliQ - Another BiliBili gRPC & REST API library

Work in process

## 快速开始

```python
import asyncio

from bilibiliq.auth import qrcode_terminal_login
from bilibiliq.grpc.dynamic import DynamicClient


async def main():
    # 在终端打印二维码登录，请确保安装 qrcode 扩展
    # pip install bilibiliq[qrcode]
    # pdm install -G qrcode
    auth = await qrcode_terminal_login()
    async with DynamicClient(auth) as client:
        dynamics = await client.get_user_dynamics(
            478775392
        )  # 获取 UID 为 478775392 的用户的动态
        print(dynamics.dict())


if __name__ == "__main__":
    asyncio.run(main())
```

## 命令行程序

```text
$ bilibiliq-auth
usage: bilibiliq-auth [-h] [-c {tv,web}] [-s [SAVE_FILE]] {sms,password,qrcode} ...

BiliBiliQ 命令行程序，可用于获取或保存鉴权信息，供程序使用
支持短信登录，密码登录，扫码登录（需安装 qrcode 扩展）
允许指定客户端类型为 TV 或 Web（使用 -c 传入，默认为 tv）

短信登录必须传入手机号，可选传入国际区号
  bilibiliq-auth sms <手机号> [国际区号]
  e.g. bilibiliq-auth sms 1xxxxxxxxx0 +86
密码登录必须传入账号（手机号或邮箱），密码
  bilibiliq-auth password <账号> <密码>
  e.g. bilibiliq-auth password 1xxxxxxxxx0 12345678
短信登录和密码登录需要进行 geetest 验证，可前往 https://kuresaru.github.io/geetest-validator
输入提供的 gt 和 challenge 进行验证并将返回的 validate 传入程序

扫码登录需安装 qrcode 扩展，可使用如下命令安装
  pip install bilibiliq[qrcode]  # 使用 pip
  pdm install -G qrcode  # 使用 pdm
扫码登录无需传入参数
  bilibiliq-auth qrcode
使用哔哩哔哩客户端扫描在终端打印的二维码即可，若二维码失效可结束程序再登录

-s 参数用于保存鉴权信息到 json 文件
如果不传入参数，则默认以 <登录账号 UID>.json 的名称保存到用户数据目录
  macOS:     ~/Library/Application Support/BiliBiliQ
  Unix:      ~/.local/share/BiliBiliQ (XDG default)
  Windows:   C:\Users\<username>\AppData\Local\BiliBiliQ\BiliBiliQ
如果传入参数，则以参数为文件名保存文件
保存后的文件可使用 `Auth.load_from_file` 读取
下方为示例及对应的读取代码

  不传入参数：
    bilibiliq-auth -s qrcode
    -----------------------------
    from bilibiliq.auth import Auth

    auth = Auth.load_from_file(uid=<登录账号的UID>)

  传入参数：
    bilibiliq-auth -s ./auth.json qrcode
    -----------------------------------------
    from pathlib import Path

    from bilibiliq.auth import Auth

    auth = Auth.load_from_file(Path("./auth.json"))

positional arguments:
  {sms,password,qrcode}
                        登录方式
    sms                 短信登录
    password            密码登录
    qrcode              密码登录

options:
  -h, --help            show this help message and exit
  -c {tv,web}, --client-type {tv,web}
                        客户端类型：TV端（返回可用于 gRPC 请求），Web端
  -s [SAVE_FILE], --save-file [SAVE_FILE]
                        保存鉴权信息
```

```text
$ bilibiliq-auth -s -c tv qrcode

请使用哔哩哔哩客户端扫描下方二维码


    █▀▀▀▀▀█ ▀ ▀▄▀█▄█▀ ▄▀█ ▄▄▄▀▀▀▄█▀  ▀ ▄▀ █▀▀▀▀▀█
    █ ███ █ ▄▄██▀▀ ▄▀▄▀▀▄▄▀▀▄▀█▀▄▄▀▀▀█ █▄ █ ███ █
    █ ▀▀▀ █ █▄▀▀ ▄▀██▀▄▄█▀▀▀█▄▄██▀▀▄▄█▀▀▀ █ ▀▀▀ █
    ▀▀▀▀▀▀▀ █▄█▄█▄█▄█ ▀▄█ ▀ █▄█▄▀▄▀ █▄█ ▀ ▀▀▀▀▀▀▀
    ▀▄▄ █ ▀█▀█▀▄  ▄▀▀▄█ ▀▀▀▀█▀██ ██ █▄ ▄▄█████  ▀
     ▄▄█▄█▀█▀█  ▀ ▄▀  ▀▄▄▀▄▄█ █▀▄█▀▀█▀▄ █▀▀▀▀ ▀▀
     ▄▄▀██▀▀▀█▄▄▀ ██▀ ▀▀  ▀▀ ██▄ ▀█ █  █▄ ▄▄▄█▄█
     ██ ▀▀▀ █ ▄▄ ██▄▄ █▀▀▄█▄▄█▀▀▀█ ▀██▄█▀█▀ ▀▀ ▀▄
     █▀█▄▀▀█▄  ▀ ██ █▀▀ █▀▄▄▀▄█▄▄▄▄▄██▀█▄ ██  ▄ ▀
    ▀█▀▄▀ ▀▀█▄▀▄▄████▄ ▄▀▄█  ▀▀▄▀ █ ▄▀▄ █▀▀▀▀  █
     ████▀▀▀█▄▀▀ ▀▀▀ ▀▀██▀▀▀█▄█ ▄█▄ █▀ ▄█▀▀▀█▄▄▄▀
    ▀████ ▀ ██▄▀▀█▀ ▀▄█▀█ ▀ █▀▄▄ ▀▀▄▄▄▄▄█ ▀ █▀
     ▄▀ ██▀▀█▀▄█▀▀ █▄▀▄▀▀▀█▀█ █▀▄▀█▀██ ▀████▀▀▄█
    ▀ ▀▀▀ ▀▄█▀▄▄ ▀ ▄█▄█▄▀▀▀▀▀▄▀██ █▀▄  ▄█▀▄▄▄▀ █▄
    ▄ █ ▀▀▀▄▀█▄▀ ██▀█▀██▄▀▄▀▀▄█▀█▄ █▀█  ██ █▀  ▀
    █▀▀█  ▀▀▄▄▄▀   ▀ █▄ ▀ █▄  █  ▀ █▄   █ ▄███  ▄
    ██▄█▄█▀ ██  ▄█ ▀██ ▀▄▄▄▀█▀█   █ ▀█▀▄ ██▀▀█▄▀▀
     ▄▄▄█ ▀▄▄█ ██ ▄  █▀ ▀▄ ▄▀▄█▄▀▀▀▄▄█▄  ▀▄▄█▄ █
    ▀  ▀▀ ▀ ▄▀ ▄▄▄▄  █▀▄█▀▀▀█▀ █ █▄▀██▀▄█▀▀▀██▄▀▀
    █▀▀▀▀▀█ ▀▄▄ █▄▀█  ▄██ ▀ █  █ █▀▀▄█▄ █ ▀ █▀ █▄
    █ ███ █ ▀▄▀▄█▄█ ▄ ▄▀▀██▀█▀▄▀▄ █▄██▀█▀▀█▀█▀▄▄
    █ ▀▀▀ █  █▄ █▄▄ ▀█▄▀█▀▀ ▄▄█ ▄▄▀█▄ ▄▀ ▄  ▀  ▀
    ▀▀▀▀▀▀▀ ▀ ▀▀   ▀  ▀ ▀ ▀▀▀    ▀▀ ▀   ▀▀ ▀▀▀  ▀


MingxuanGame（UID：478775392）登录成功！

已保存鉴权信息到 C:\Users\Mingx\AppData\Local\BiliBiliQ\BiliBiliQ\478775392.json，可使用 `Auth.load_from_file(uid=478775392)` 读取
```

## 参考

[哔哩哔哩-API收集整理（SocialSisterYi/bilibili-API-collect）](https://github.com/SocialSisterYi/bilibili-API-collect)

[SK-415/bilireq](https://github.com/SK-415/bilireq)

## 许可

BiliBiliQ 使用 MIT 许可证开源

许可证文件：[LICENSE](./LICENSE)
