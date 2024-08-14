from tortoise import Tortoise
from rich.console import Console


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
            Console().print_exception(show_locals=True)

    async def db_disconnect(self) -> None:
        """
        Disconnect from the database.
        """
        try:
            await Tortoise.close_connections()

        except Exception:
            Console().print_exception(show_locals=True)
