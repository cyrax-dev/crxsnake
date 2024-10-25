import os
import sys

from datetime import datetime

red = 16711680
green = 65280
blue = 255
yellow = 16776960
purple = 9109759
trans = 2829617

timestamp = int(datetime.now().timestamp())
time_short = f"<t:{timestamp}:d>"
time_long_date = f"<t:{timestamp}:D>"
time_short_time = f"<t:{timestamp}:t>"
time_long_time = f"<t:{timestamp}:T>"
time_full = f"<t:{timestamp}:f>"
time_relative = f"<t:{timestamp}:R>"


async def restart():
    python = sys.executable
    os.execl(python, python, '-B', *sys.argv)
