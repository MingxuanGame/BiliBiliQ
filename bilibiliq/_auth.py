import sys
import time
from pathlib import Path
from typing import Optional

from pydantic import BaseModel
from appdirs import user_data_dir

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class Auth(BaseModel):
    DedeUserID: Optional[str] = None
    DedeUserID__ckMd5: Optional[str] = None
    SESSDATA: Optional[str] = None
    bili_jct: Optional[str] = None
    sid: Optional[str] = None
    refresh_token: Optional[str] = None
    access_token: Optional[str] = None

    def save_to_file(
        self, path: Optional[Path] = None, uid: Optional[int] = None
    ) -> Path:
        if not path:
            dir_ = Path(user_data_dir("BiliBiliQ"))
            if not dir_.exists():
                dir_.mkdir(parents=True)

            path = dir_ / (
                f"{uid}.json"
                if uid
                else f"bilibiliq_auth_{int(time.time())}.json"
            )
        with open(path, "w") as f:
            f.write(self.json())
        return path

    @classmethod
    def load_from_file(
        cls,
        path: Optional[Path] = None,
        uid: Optional[int] = None,
        timestamp: Optional[int] = None,
    ) -> Self:
        if not path:
            if uid and timestamp:
                raise ValueError("Cannot read the file by uid and timestamp")
            elif uid:
                name = f"{uid}.json"
            elif timestamp:
                name = f"bilibiliq_auth_{timestamp}.json"
            else:
                raise ValueError("No way to read the file.")

            dir_ = Path(user_data_dir("BiliBiliQ"))
            path = dir_ / name
        return cls.parse_file(path)
