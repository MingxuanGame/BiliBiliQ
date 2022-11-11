from http.cookies import SimpleCookie
from typing import Any, Tuple, Literal

from yarl import URL
from aiohttp import ClientSession

from bilibiliq.typing import AnyDict
from bilibiliq.exception import raise_for_code


async def request(
    domain: str, endpoint: str, method: Literal["GET", "POST"], **kwargs: Any
) -> Tuple[AnyDict, SimpleCookie]:
    headers = kwargs.pop("headers", {})
    for k, v in headers.items():
        headers[k] = v.lower()
    headers.setdefault(
        "user-agent",
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/106.0.0.0 "
            "Safari/537.36 Edg/106.0.1370.52"
        ),
    )
    async with ClientSession() as session:
        resp = await session.request(
            method, URL(domain) / endpoint, headers=headers, **kwargs
        )
        resp.raise_for_status()
        data = await resp.json()
        raise_for_code(data["code"], data["message"])
        return data["data"] or {}, resp.cookies


async def request_passport(
    endpoint: str, method: Literal["GET", "POST"], **kwargs: Any
) -> Tuple[AnyDict, AnyDict]:
    return await request(
        "https://passport.bilibili.com", endpoint, method, **kwargs
    )
