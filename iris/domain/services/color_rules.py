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

import colorsys
from iris.domain.entities.palette import Color, Palette

def complementary_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    comp_h = (h + 0.5) % 1.0
    return Palette([
        Color.from_tuple(base_color),
        Color.from_tuple(hsv_to_rgb(comp_h, s, v))
    ])

def triadic_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    h1 = (h + 1/3) % 1.0
    h2 = (h + 2/3) % 1.0
    return Palette([
        Color.from_tuple(base_color),
        Color.from_tuple(hsv_to_rgb(h1, s, v)),
        Color.from_tuple(hsv_to_rgb(h2, s, v))
    ])

def analogous_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    h1 = (h + 1/12) % 1.0
    h2 = (h - 1/12) % 1.0
    return Palette([
        Color.from_tuple(base_color),
        Color.from_tuple(hsv_to_rgb(h1, s, v)),
        Color.from_tuple(hsv_to_rgb(h2, s, v))
    ])

def monochromatic_dark_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    factors = [1.0, 0.4, 0.3, 0.2, 0.1, 0.05]
    return Palette([
        Color.from_tuple(hsv_to_rgb(h, s, v * f)) for f in factors
    ])

def monochromatic_light_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    steps = 6
    diff = 1.0 - v
    step = diff / (steps - 1)
    return Palette([
        Color.from_tuple(hsv_to_rgb(h, s - s * 0.16 * i, v + step * i)) for i in range(steps)
    ])

def accent_analogous_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    h_analog = (h + 1/12) % 1.0
    h_accent = (h + 1/6) % 1.0
    h_complement = (h_accent + 0.5) % 1.0
    return Palette([
        Color.from_tuple(base_color),
        Color.from_tuple(hsv_to_rgb(h_analog, s, v)),
        Color.from_tuple(hsv_to_rgb(h_accent, s, v)),
        Color.from_tuple(hsv_to_rgb(h_complement, s, v))
    ])

def tetrad_colors(base_color: tuple[int, int, int]) -> Palette:
    h, s, v = rgb_to_hsv(*base_color)
    h1 = (h + 0.25) % 1.0
    h2 = (h + 0.5) % 1.0
    h3 = (h + 0.75) % 1.0
    return Palette([
        Color.from_tuple(base_color),
        Color.from_tuple(hsv_to_rgb(h1, s, v)),
        Color.from_tuple(hsv_to_rgb(h2, s, v)),
        Color.from_tuple(hsv_to_rgb(h3, s, v))
    ])

def rgb_to_hsv(r: int, g: int, b: int) -> tuple[float, float, float]:
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

def hsv_to_rgb(h: float, s: float, v: float) -> tuple[int, int, int]:
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_to_hsl(rgb: tuple) -> tuple:
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (
        round(h * 360),   
        round(s * 100),    
        round(l * 100))

def lighten_color_hsv(color, factor=0.2):
    r, g, b = [c/255.0 for c in color]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    
    v = min(1.0, v + factor)
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (int(r*255), int(g*255), int(b*255))

def lighten_color_rgb(color, factor=0.2):

    if isinstance(color, tuple) and len(color) == 3:
        r, g, b = color
    elif isinstance(color, (int, float)):
        color_int = int(color)
        r = (color_int >> 16) & 0xFF
        g = (color_int >> 8) & 0xFF
        b = color_int & 0xFF
    elif isinstance(color, str) and color.startswith('#'):
        color = color.lstrip('#')
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
    else:
        raise ValueError(f"Unsupported color format: {color}")
    
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return (r, g, b)
