from .logger import log
from tortoise import Tortoise


class Database:

    def __init__(self, db_url: str):
        self.db_url = db_url

    async def db_connect(self) -> None:
        try:
            await Tortoise.init(
                db_url=self.db_url,
                modules={
                    "models": ["src.utils"]
                }
            )
            await Tortoise.generate_schemas()
            log.info("[Database] SqLite connected")

        except Exception as e:
            log.error(f"[Database] Failed to connect SqLite: {e}")

    @staticmethod
    async def disconnect_db() -> None:
        await Tortoise.close_connections()
