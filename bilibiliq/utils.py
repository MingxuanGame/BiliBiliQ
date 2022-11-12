import random
import hashlib
from copy import deepcopy
from typing import Tuple, Optional

from bilibiliq._auth import Auth
from bilibiliq.internal.pb.bilibili.metadata.metadata_pb2 import Metadata
from bilibiliq.internal.pb.bilibili.metadata.device.device_pb2 import Device
from bilibiliq.internal.pb.bilibili.metadata.locale.locale_pb2 import Locale
from bilibiliq.internal.pb.bilibili.metadata.network.network_pb2 import (
    Network,
    NetworkType,
)


def fake_buvid():
    mac_list = []
    for _ in range(1, 7):
        rand_str = "".join(random.sample("0123456789abcdef", 2))
        mac_list.append(rand_str)
    rand_mac = ":".join(mac_list)
    md5 = hashlib.md5()
    md5.update(rand_mac.encode())
    md5_mac_str = md5.hexdigest()
    md5_mac = list(md5_mac_str)
    fake_mac = (
        "XY" + md5_mac[2] + md5_mac[12] + md5_mac[22] + md5_mac_str
    ).upper()
    return fake_mac


BUVID = fake_buvid()


def make_metadata(
    auth: Optional[Auth] = None,
) -> Tuple[Tuple[str, bytes], ...]:
    if auth and auth.access_token:
        access_token = auth.access_token
    else:
        access_token = ""
    device = {
        "build": 6550400,
        "buvid": BUVID,
        "mobi_app": "android",
        "platform": "android",
        "channel": "bili",
        "device": "phone",
    }
    metadata = deepcopy(device)
    metadata["access_key"] = access_token

    metadata_ = {
        "x-bili-device-bin": Device(**device).SerializeToString(),
        "x-bili-local-bin": Locale().SerializeToString(),
        "x-bili-metadata-bin": Metadata(**metadata).SerializeToString(),
        "x-bili-network-bin": Network(
            type=NetworkType.WIFI
        ).SerializeToString(),
    }
    if access_token:
        metadata_["authorization"] = f"identify_v1 {access_token}".encode()
    return tuple(metadata_.items())
