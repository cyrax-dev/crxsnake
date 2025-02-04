from typing import Optional, Tuple, List
from disnake import TextChannel, User, Embed, Forbidden, HTTPException


class EmbedLog:

    @staticmethod
    def build_embed(
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

    async def send_channel(self, channel: TextChannel, **kwargs) -> None:
        embed = self.build_embed(**kwargs)
        try:
            await channel.send(embed=embed)
        except Forbidden:
            print(f"[Ошибка] Нет прав на отправку сообщений в канал {channel.name}.")
        except HTTPException as e:
            print(f"[Ошибка] Не удалось отправить сообщение: {e}")

    async def send_user(self, user: User, **kwargs) -> None:
        embed = self.build_embed(**kwargs)
        try:
            await user.send(embed=embed)
        except Exception:
            pass
