class BiliBiliError(Exception): ...


class RESTError(BiliBiliError):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"<RESTException code={self.code}, message={self.message}>"


class NeedVerify(BiliBiliError):
    # 2：本次登录环境存在风险, 需使用手机号进行验证或绑定
    ...


class QRCodeExpired(BiliBiliError):
    # 86038：二维码已失效
    ...


class QRCodeNotAccepted(BiliBiliError):
    # 86090：二维码已扫码未确认
    # 86039：二维码尚未确认
    ...


class NotScanQRCode(BiliBiliError):
    # 86101：未扫码
    ...


def raise_for_code(code: int, message: str) -> None:
    if code != 0:
        raise RESTError(code, message)
