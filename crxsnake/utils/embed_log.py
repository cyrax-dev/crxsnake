from typing import Optional, Tuple, List, NoReturn
from disnake import TextChannel, User, Embed, Forbidden, HTTPException


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
        """Создает Embed с заданными параметрами."""
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
        fields: Optional[List[Tuple[str, str, bool]]] = None,
        desc: Optional[str] = None,
        url: Optional[str] = None,
        thumbnail: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None,
        custom_embed: Optional[Embed] = None,
    ) -> None:
        embed = custom_embed or self.build_embed(
            title, color, fields, desc, url, thumbnail, image, footer
        )
        try:
            await channel.send(embed=embed)
        except Forbidden:
            print(f"[Ошибка] Нет прав на отправку сообщений в канал {channel.name}")
        except HTTPException as e:
            print(f"[Ошибка] Не удалось отправить сообщение: {e}")

    async def send_user(
        self,
        user: User,
        title: Optional[str] = None,
        color: Optional[int] = None,
        fields: Optional[List[Tuple[str, str, bool]]] = None,
        desc: Optional[str] = None,
        url: Optional[str] = None,
        thumbnail: Optional[str] = None,
        image: Optional[str] = None,
        footer: Optional[str] = None,
        custom_embed: Optional[Embed] = None,
    ) -> None:
        embed = custom_embed or self.build_embed(
            title, color, fields, desc, url, thumbnail, image, footer
        )
        try:
            await user.send(embed=embed)
        except Exception:
            pass
