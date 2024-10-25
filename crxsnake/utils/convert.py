from hashlib import sha256, md5
from base64 import b64encode


def steam_to_be_guid(steam_id: int) -> str:
    parts = [0x42, 0x45] + [0] * 8
    for i in range(2, 10):
        steam_id, remainder = divmod(steam_id, 256)
        parts[i] = remainder

    byte_array = bytes(parts)
    hash_object = md5(byte_array)
    return hash_object.hexdigest()


def steam_to_dayz_guid(steam_id: int) -> str:
    hashed = sha256()
    hashed.update(str(steam_id).encode("utf-8"))
    return b64encode(hashed.digest()).decode("utf-8")
