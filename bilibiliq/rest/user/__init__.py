from typing import Optional

from bilibiliq.auth import Auth
from bilibiliq.rest.user.model import SelfInfo
from bilibiliq.internal.client import BaseRESTClient


class UserClient(BaseRESTClient):
    def __init__(self, auth: Optional[Auth] = None) -> None:
        super().__init__(auth)

    async def get_self_info(self) -> SelfInfo:
        if self.auth is None:
            raise ValueError("Auth is None, cannot get self-information.")
        return SelfInfo.parse_obj(
            (await self.request_api("x/space/myinfo", "GET"))[0]
        )
