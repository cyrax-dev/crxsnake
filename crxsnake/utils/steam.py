import re
import json

from aiohttp import ClientError

from crxsnake.web.request import Request
from crxsnake.logger import log


async def get_steam_id(steam_profile_url: str) -> int | None:
    """Get steam id from steam profile url.

    Args:
        steam_profile_url (str)
    Returns:
        int | None
    """
    async with Request() as steam:
        try:
            response = await steam.request(steam_profile_url)
            if not response:
                return None

            data_match = re.search(r"g_rgProfileData\s*=\s*(?P<json>{.*?});", response)
            if data_match:
                return int(json.loads(data_match.group("json"))["steamid"])

        except ClientError as e:
            log.error("Error during request", "Steam", e)
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            log.error("Error during data processing", "Steam", e)

    return None
