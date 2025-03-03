from typing import Optional, Tuple, List
from disnake import TextChannel, User, Embed, Forbidden, HTTPException
from crxsnake.logger import log


class EmbedLog:

    @classmethod
    def build_embed(
        cls,
        title: Optional[str] = None,
        color: Optional[int] = None,
        fields: Optional[List[Tuple[str, str, bool]]] = None,
        desc: Optional[str] = None,
        url: Optional[str] = None,
        thumbnail: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None,
    ) -> Embed:

        embed = Embed(title=title, description=desc, color=color, url=url)
        if fields:
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        if image:
            embed.set_image(url=image)
        if footer:
            embed.set_footer(text=footer)

        return embed

    async def send_channel(
        self,
        channel: TextChannel,
        title: Optional[str] = None,
        color: Optional[int] = None,
        content: Optional[str] = None,
        fields: Optional[List[Tuple[str, str, bool]]] = None,
        desc: Optional[str] = None,
        url: Optional[str] = None,
        thumbnail: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None
    ) -> None:

        try:
            embed = self.build_embed(title, color, fields, desc, url, thumbnail, image, footer)
            await channel.send(content=content, embed=embed)
        except Forbidden:
            log.error("Not enough permissions to send embed", "LogEmbed")
        except HTTPException as e:
            log.error("Error when sending embed", "LogEmbed", e)

    async def send_user(
        self,
        user: User,
        title: Optional[str] = None,
        color: Optional[int] = None,
        content: Optional[str] = None,
        fields: Optional[List[Tuple[str, str, bool]]] = None,
        desc: Optional[str] = None,
        url: Optional[str] = None,
        thumbnail: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None
    ) -> None:
        try:
            embed = self.build_embed(title, color, fields, desc, url, thumbnail, image, footer)
            await user.send(content=content, embed=embed)
        except Exception:
            pass
