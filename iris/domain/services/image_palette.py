# ─────────────────────────────────────────────────────────────
# Iris — генератор цветовых палитр
# (c) 2025 Mitori Vancody Firelight
#
# Разработка и код: Mitori Vancody Firelight
# Связаться со мной:
#   VK:        https://vk.com/mitori_territory
#   Telegram:  https://t.me/Vancody_Firelight
#   GitHub:    https://github.com/Vancody
#   Discord:   @vancodyfirelight
#
# Этот код распространяется без лицензии, но с сохранением авторства.
# Копирование и использование разрешено при указании автора.
# ─────────────────────────────────────────────────────────────

from colorthief import ColorThief
from iris.domain.entities.palette import Palette, Color

def generate_palette_from_image(filename: str, color_count: int = 6) -> Palette:
    color_thief = ColorThief(filename)
    raw_colors = color_thief.get_palette(color_count=color_count)
    colors = [Color.from_tuple(rgb) for rgb in raw_colors]
    return Palette(colors, name=f"From {filename}")
