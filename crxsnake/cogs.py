from loguru import logger

from sys import path
from pathlib import Path


async def load_cogs(bot) -> None:
    directory_path = Path("src")
    path.append(str(directory_path))

    for entry in directory_path.iterdir():
        for filename in entry.iterdir():
            if filename.suffix == ".py" and entry.name != "utils":
                try:
                    bot.load_extension(f"{entry.name}.{filename.stem}")
                except Exception:
                    logger.exception(f"An error occurred while loading cog {entry.name}.{filename.stem}")
