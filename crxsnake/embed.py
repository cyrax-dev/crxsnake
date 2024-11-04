from disnake import Embed, Forbidden, Color
from disnake.ext import commands


class Embed:

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def send_channel(self, channel_id: int, title: str, desc: str, color: Color):
        channel = await self.bot.fetch_channel(channel_id)
        if channel:
            embed = self.__create_embed(title, desc, color)
            await channel.send(embed=embed)

    async def send_user(self, user_id: int, title: str, desc: str, color: Color):
        try:
            user = await self.bot.fetch_user(user_id)
            if user:
                embed = self.__create_embed(title, desc, color)
                await user.send(embed=embed)
        except Forbidden:
            pass

    def __create_embed(self, title: str, desc: str, color: Color):
        return Embed(title=title, description=desc, color=color)
