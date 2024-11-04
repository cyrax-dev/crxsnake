import re
import os
import sys

from datetime import datetime
from disnake import Embed


red = 16711680
green = 65280
blue = 255
yellow = 16776960
purple = 9109759
trans = 2829617


def restart():
    python = sys.executable
    os.execl(python, python, '-B', *sys.argv)


def get_unix_time() -> int:
    return int(datetime.now().timestamp())


def get_user_id(field_index: int, embed: Embed) -> int:
    user_id_str = re.search(r"<@!?(\d+)>", embed.fields[field_index].value).group(1)
    return int(user_id_str)
