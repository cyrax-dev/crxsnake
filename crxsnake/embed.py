from typing import Optional, Dict, Any

from disnake import Embed, Forbidden, Colour
from disnake.ext import commands
from crxsnake.utils.misc import trans


class EmbedMessage:

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def send_channel(
        self,
        channel_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        color: Optional[Colour] = trans,
        url: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None
    ) -> None:
        """Send an Embed message to the channel"""
        channel = await self.bot.fetch_channel(channel_id)
        if channel:
            embed = self.__create_embed(
                title,
                description,
                color,
                url,
                image,
                footer,
                fields
            )
            await channel.send(embed=embed)

    async def send_user(
        self,
        user_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        color: Optional[Colour] = trans,
        url: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None
    ) -> None:
        """Send an Embed message to the user"""
        try:
            user = await self.bot.fetch_user(user_id)
            if user:
                embed = self.__create_embed(
                    title,
                    description,
                    color,
                    url,
                    image,
                    footer,
                    fields
                )
                await user.send(embed=embed)
        except Forbidden:
            pass

    @staticmethod
    def __create_embed(
        title: Optional[str] = None,
        description: Optional[str] = None,
        color: Optional[Colour] = trans,
        url: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None
    ) -> Embed:
        """Return Embed"""
        embed = Embed(
            title=title,
            description=description,
            url=url,
            color=color
        )
        if image:
            embed.set_image(url=image)
        if footer:
            embed.set_footer(text=footer)
        if fields:
            for name, value in fields.items():
                embed.add_field(name=name, value=value, inline=False)
        return embed
