import sys
from types import TracebackType
from http.cookies import SimpleCookie
from typing import Any, Type, Tuple, Literal, Optional

import grpc
from yarl import URL
from aiohttp import ClientSession
from google.protobuf.message import Message
from google.protobuf.json_format import MessageToDict

from bilibiliq._auth import Auth
from bilibiliq.typing import AnyDict
from bilibiliq.utils import make_metadata
from bilibiliq.exception import raise_for_code

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class BaseRESTClient:
    def __init__(self, auth: Optional[Auth] = None) -> None:
        self.auth = auth
        self.session = ClientSession()

    async def rest_request(
        self,
        domain: str,
        endpoint: str,
        method: Literal["GET", "POST"],
        auth: Optional[Auth] = None,
        **kwargs: Any,
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
        params = kwargs.pop("params", None)
        if auth is None:
            auth = self.auth
        if auth is not None:
            headers.setdefault(
                "cookie",
                " ".join(
                    [
                        f"{k}={v};"
                        for k, v in auth.dict(exclude_none=True).items()
                    ]
                ),
            )
            if access_key := auth.access_token:
                if params:
                    params["access_key"] = access_key
                else:
                    params = {"access_key": access_key}
        resp = await self.session.request(
            method,
            URL(domain) / endpoint,
            headers=headers,
            params=params,
            **kwargs,
        )
        resp.raise_for_status()
        data = await resp.json()
        raise_for_code(data["code"], data["message"])
        return data["data"] or {}, resp.cookies

    async def request_api(
        self,
        endpoint: str,
        method: Literal["GET", "POST"],
        auth: Optional[Auth] = None,
        **kwargs: Any,
    ) -> Tuple[AnyDict, AnyDict]:

        return await self.rest_request(
            "https://api.bilibili.com", endpoint, method, auth, **kwargs
        )

    async def request_vc_api(
        self,
        endpoint: str,
        method: Literal["GET", "POST"],
        auth: Optional[Auth] = None,
        **kwargs: Any,
    ) -> Tuple[AnyDict, AnyDict]:

        return await self.rest_request(
            "https://api.vc.bilibili.com", endpoint, method, auth, **kwargs
        )

    async def request_message_api(
        self,
        endpoint: str,
        method: Literal["GET", "POST"],
        auth: Optional[Auth] = None,
        **kwargs: Any,
    ) -> Tuple[AnyDict, AnyDict]:

        return await self.rest_request(
            "https://message.bilibili.com", endpoint, method, auth, **kwargs
        )

    def set_auth(self, auth: Auth) -> None:
        self.auth = auth

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def close(self):
        await self.session.close()


async def request_passport(
    endpoint: str, method: Literal["GET", "POST"], **kwargs: Any
) -> Tuple[AnyDict, AnyDict]:
    async with BaseRESTClient() as client:
        return await client.rest_request(
            "https://passport.bilibili.com", endpoint, method, **kwargs
        )


class BaseGrpcClient:
    def __init__(self, auth: Optional[Auth] = None) -> None:
        self.auth = auth
        self.metadata = make_metadata(auth)
        self.channel = grpc.aio.secure_channel(
            "grpc.biliapi.net", grpc.ssl_channel_credentials()
        )

    async def grpc_request(
        self,
        stub: Type[Any],
        service: str,
        request: Message,
        auth: Optional[Auth] = None,
    ) -> Any:
        metadata = make_metadata(auth) if auth else self.metadata
        return await getattr(stub(self.channel), service)(
            request, metadata=metadata
        )

    async def grpc_request_dict(
        self,
        stub: Type[Any],
        service: str,
        request: Message,
        auth: Optional[Auth] = None,
    ) -> Any:
        return MessageToDict(
            await self.grpc_request(stub, service, request, auth),
            including_default_value_fields=True,
            preserving_proto_field_name=True,
        )

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    def set_auth(self, auth: Auth) -> None:
        self.auth = auth

    async def close(self) -> None:
        await self.channel.close()
