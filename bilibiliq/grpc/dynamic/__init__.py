from typing import Optional

from bilibiliq.auth import Auth
from bilibiliq.internal.client import BaseGrpcClient
from bilibiliq.internal.pb.bilibili.app.dynamic.v2.dynamic_pb2 import (
    DynSpaceReq,
)
from bilibiliq.internal.pb.bilibili.app.dynamic.v2.dynamic_pb2_model import (
    DynSpaceRsp,
)
from bilibiliq.internal.grpc.bilibili.app.dynamic.v2.dynamic_pb2_grpc import (
    DynamicStub,
)


class DynamicClient(BaseGrpcClient):
    def __init__(self, auth: Optional[Auth] = None) -> None:
        super().__init__(auth)

    async def get_user_dynamics(
        self, uid: int, offset: str = "", page: int = 1
    ) -> DynSpaceRsp:
        req = DynSpaceReq(host_uid=uid, history_offset=offset, page=page)
        return DynSpaceRsp.parse_obj(
            await self.grpc_request_dict(DynamicStub, "DynSpace", req)
        )
