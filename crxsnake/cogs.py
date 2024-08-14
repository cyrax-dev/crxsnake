from sys import path
from pathlib import Path
from rich.console import Console


async def load_cogs(bot, directory="src"):
    directory_path = Path(directory)
    path.append(str(directory_path))

    for entry in directory_path.iterdir():
        for filename in entry.iterdir():
            if filename.suffix == ".py" and entry.name != "utils":
                try:
                    bot.load_extension(f"{entry.name}.{filename.stem}")
                except Exception:
                    Console().print_exception(show_locals=True)
