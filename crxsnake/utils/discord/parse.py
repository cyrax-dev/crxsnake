import re
from disnake import Embed


def get_user_id(field_index: int, embed: Embed) -> int:
    """Gets the user ID from the specified field index in the given embed.
    Args:
        field_index (int): Field index.
        embed (Embed): Embed object.
    Returns:
        int: DiscordID
    """
    user_id_str = re.search(r"<@!?(\d+)>", embed.fields[field_index].value).group(1)
    return int(user_id_str)
