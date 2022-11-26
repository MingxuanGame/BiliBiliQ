from typing import List

from bilibiliq.internal.client import BaseRESTClient

from .model import Emoji


async def get_e_infos(client: BaseRESTClient) -> List[Emoji]:
    emojis = []
    data = (
        await client.request_api(
            "x/emote/user/panel/web", "GET", params={"business": "reply"}
        )
    )[0]
    for packages in data["packages"]:
        emojis.extend(
            Emoji(
                text=emoji["text"],
                url=emoji["url"],
                size=emoji["meta"]["size"],
            )
            for emoji in packages["emote"]
        )
    return emojis
