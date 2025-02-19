from pathlib import Path
from disnake.ext.commands import Bot
from crxsnake.logger import log


async def load_cogs(bot: Bot, folder: str = "src", utils: str = "utils"):
    """Loads cogs (extensions) for the bot from the specified folder.
    Args:
        bot (Bot): The bot instance.
        folder (str, optional): The main folder containing the cogs. Defaults to "src".
        utils (str, optional): The name of the utilities folder to exclude. Defaults to "utils".

    Raises:
        Exception: If an error occurs while loading cogs.
    """
    try:
        base_path = Path.cwd() / folder

        for entry in base_path.iterdir():
            if entry.is_dir() and entry.name != utils:
                for filename in entry.glob("*.py"):
                    bot.load_extension(f"{folder}.{entry.name}.{filename.stem}")

        log.info("Cogs successfully loaded", "Discord")

    except Exception as e:
        log.error(f"An error occurred while loading modules", "Discord", e)
