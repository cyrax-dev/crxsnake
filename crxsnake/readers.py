import re
import aiofiles

from typing import Optional, Any
from json import loads, dumps


async def read_json(path: str, *keys: str) -> Optional[Any]:
    """Read data from a JSON file.
    Args:
        path (str): Json file path
        *keys (str): Keys to read from the JSON file
    Returns:
        Optional[Dict]:
    """
    try:
        async with aiofiles.open(path, "r", encoding="utf-8") as file:
            file_content = await file.read()
            file_data = loads(file_content)

            for key in keys:
                file_data = file_data.get(key)
                if file_data is None:
                    return None
            return file_data
    except Exception:
        raise


async def write_json(path: str, data: Any) -> bool:
    """Write data to a JSON file.
    Args:
        path (str): Json file path
        data (Any): Data to write to the JSON file
    Returns:
        bool: True if the data was written successfully, False otherwise
    """
    try:
        async with aiofiles.open(path, "w", encoding="utf-8") as file:
            await file.write(dumps(data, ensure_ascii=False, indent=2))
            return True
    except Exception:
        raise


async def read_jsonc(path: str, *keys: str) -> Optional[Any]:
    """Read data from a JSONC file.
    Args:
        path (str): Json file path
        *keys (str): Keys to read from the JSON file
    Returns:
        Optional[Dict]: Data read from the JSON file
    """
    try:
        regex = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*)", re.MULTILINE | re.DOTALL)

        def __re_sub(match):
            return match.group(1) or ""

        async with aiofiles.open(path, "r", encoding="utf-8") as file:
            file_content = regex.sub(__re_sub, await file.read())
            file_data = loads(file_content)

            for key in keys:
                file_data = file_data.get(key)
                if file_data is None:
                    return None
            return file_data
    except Exception:
        raise
