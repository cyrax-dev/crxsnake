from logger import log
from tortoise import Tortoise


class Database:
    DB_URL = "sqlite://settings/database/database.db"
    DB_MODEL = {"models": ["src.utils"]}

    @staticmethod
    async def db_connect() -> None:
        try:
            await Tortoise.init(db_url=Database.DB_URL, modules=Database.DB_MODEL)
            await Tortoise.generate_schemas()
            log.info("[Database] SqLite connected")

        except Exception as e:
            log.error(f"[Database] Failed to connect SqLite: {e}")

    @staticmethod
    async def disconnect_db() -> None:
        await Tortoise.close_connections()
