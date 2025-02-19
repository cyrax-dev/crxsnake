from aiohttp import ClientSession, ClientTimeout, ClientError
from crxsnake.logger import log


class Request:
    TIMEOUT = ClientTimeout(total=20)
    STEAM_USER_AGENT = "python-steam/1.4.4"

    def __init__(self, user_agent: str = None):
        self.session = None
        self.user_agent = {"User-Agent": user_agent or self.STEAM_USER_AGENT}

    async def __aenter__(self):
        self.session = ClientSession(headers=self.user_agent, timeout=self.TIMEOUT)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def request(self, url: str, method: str = "GET", **kwargs) -> str | None:
        """Make a request to a URL.
        Args:
            url (str): URL to request
            method (str, optional): Request method. Defaults to "GET".
        Returns:
            str | None: Response text or None if an error occurred
        """
        try:
            async with self.session.request(method, url, **kwargs) as response:
                response.raise_for_status()
                return await response.text()

        except ClientError as e:
            log.error("Error when requesting", "Request", e)
        except Exception as e:
            log.error(f"Unexpected mistake", "Request", e)
        return None
