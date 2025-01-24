from sys import path
from pathlib import Path
from logger import log


async def load_cogs(bot, folder: str = "src", utils_folder: str = "utils") -> None:
    try:
        path.append(str(Path(folder)))

        for entry in Path(folder).iterdir():
            for filename in entry.iterdir():
                if filename.suffix == ".py" and entry.name != utils_folder:
                    bot.load_extension(f"{entry.name}.{filename.stem}")

        log.info(f"[Discord] Cogs success loaded")

    except Exception as e:
        log.error(f"[Discord] An error occurred while loading modules\n╰─> Error: {e}")
