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
from typing import List


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def to_tuple(self) -> tuple:
        return (self.r, self.g, self.b)

    def to_hex(self) -> str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def to_hsv(self) -> tuple:
        return colorsys.rgb_to_hsv(self.r / 255, self.g / 255, self.b / 255)

    @staticmethod
    def from_tuple(rgb: tuple[int, int, int]) -> "Color":
        return Color(*rgb)

    def __str__(self):
        return f"{self.to_tuple()} / {self.to_hex()}"


class Palette:
    def __init__(self, colors: List[Color], name: str = "Untitled"):
        self.colors = colors
        self.name = name

    def add_color(self, color: Color):
        self.colors.append(color)

    def to_rgb_list(self) -> List[tuple]:
        return [c.to_tuple() for c in self.colors]

    def to_hex_list(self) -> List[str]:
        return [c.to_hex() for c in self.colors]

    def serialize(self) -> str:
        return ";".join(f"{c.r},{c.g},{c.b}" for c in self.colors)

    @staticmethod
    def deserialize(serialized: str) -> "Palette":
        parts = serialized.split(";")
        colors = [Color(*map(int, p.split(","))) for p in parts]
        return Palette(colors)

    def __str__(self):
        return f"Palette '{self.name}': " + ", ".join(self.to_hex_list())
