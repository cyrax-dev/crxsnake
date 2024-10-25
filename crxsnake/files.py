from loguru import logger
from aiofiles import open

from typing import Optional, Any
from json import loads, dumps


async def read_json(path: str, *keys: str) -> Optional[Any]:
    """
    Read data from json file.
    """
    try:
        async with open(path, "r", encoding="utf-8") as file:
            file_content = await file.read()
            file_data = loads(file_content)

            for key in keys:
                if key not in file_data:
                    return None
                file_data = file_data[key]

            return file_data

    except Exception:
        raise


async def write_json(path: str, data: Any) -> bool:
    """
    Write data to json file.
    """
    try:
        async with open(path, "w", encoding="utf-8") as file:
            await file.write(dumps(data, ensure_ascii=False, indent=2))
            return True
    except Exception:
        raise
