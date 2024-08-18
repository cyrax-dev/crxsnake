from loguru import logger
from tortoise import Tortoise


class Database:
    DB_URL = "sqlite://settings/database/database.db"
    DB_MODEL = {"models": ["src.utils"]}

    async def db_connect(self) -> None:
        """
        Connect to the database.
        """
        try:
            await Tortoise.init(db_url=self.DB_URL, modules=self.DB_MODEL)
            await Tortoise.generate_schemas()
        except Exception:
            logger.exception("An error occurred while connecting to the database")

    async def db_disconnect(self) -> None:
        """
        Disconnect from the database.
        """
        await Tortoise.close_connections()
