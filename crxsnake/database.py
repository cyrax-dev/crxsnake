from tortoise import Tortoise
from crxsnake.logger import log


class Database:
    DEFAULT_URL = "sqlite://settings/database/database.db"
    DEFAULT_MODELS = "src.utils"

    def __init__(self, db_url: str = None, models: str = None):
        self.db_url = db_url or self.DEFAULT_URL
        self.models = {"models": [models or self.DEFAULT_MODELS]}

    async def db_connect(self) -> None:
        """Connect to the database."""
        try:
            await Tortoise.init(db_url=self.db_url, modules=self.models)
            await Tortoise.generate_schemas()
            log.info("SqLite connected", "Database")

        except Exception as e:
            log.error("Failed to connect SqLite", "Database", e)

    @staticmethod
    async def disconnect_db() -> None:
        """Disconnect from the database."""
        await Tortoise.close_connections()
