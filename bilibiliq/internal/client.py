from typing import Any, Type, Optional

import grpc
from google.protobuf.message import Message
from google.protobuf.json_format import MessageToDict

from bilibiliq.auth import Auth
from bilibiliq.utils import make_metadata


class BaseGrpcClient:
    def __init__(self, auth: Optional[Auth] = None) -> None:
        self.auth = auth
        self.metadata = make_metadata(auth)
        self.channel = grpc.aio.secure_channel(
            "grpc.biliapi.net", grpc.ssl_channel_credentials()
        )

    async def grpc_request(
        self, stub: Type[Any], service: str, request: Message
    ) -> Any:
        return await getattr(stub(self.channel), service)(
            request, metadata=self.metadata
        )

    async def grpc_request_dict(
        self, stub: Type[Any], service: str, request: Message
    ) -> Any:
        return MessageToDict(
            await self.grpc_request(stub, service, request),
            including_default_value_fields=True,
            preserving_proto_field_name=True,
        )

    async def close(self) -> None:
        await self.channel.close()
