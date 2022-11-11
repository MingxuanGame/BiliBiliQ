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
    client = DynamicClient(auth)
    dynamics = await client.get_user_dynamics(
        478775392
    )  # 获取 UID 为 478775392 的用户的动态
    print(dynamics.dict())


if __name__ == "__main__":
    asyncio.run(main())
```

## 参考

[哔哩哔哩-API收集整理（SocialSisterYi/bilibili-API-collect）](https://github.com/SocialSisterYi/bilibili-API-collect)

[SK-415/bilireq](https://github.com/SK-415/bilireq)

## 许可

BiliBiliQ 使用 MIT 许可证开源

许可证文件：[LICENSE](./LICENSE)
