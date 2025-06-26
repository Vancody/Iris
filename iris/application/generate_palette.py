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

from iris.domain.services.color_rules import (
    complementary_colors,
    triadic_colors,
    tetrad_colors,
    analogous_colors,
    accent_analogous_colors,
    monochromatic_dark_colors,
    monochromatic_light_colors,
)
from iris.domain.services.image_palette import generate_palette_from_image
from iris.domain.entities.palette import Palette


def generate_palette(base_color: tuple[int, int, int], method: str, image_path: str | None = None) -> Palette:
    method = method.strip().lower()

    if method == "комплиментарность":
        return complementary_colors(base_color)
    elif method == "триада":
        return triadic_colors(base_color)
    elif method == "тетрада":
        return tetrad_colors(base_color)
    elif method == "аналогия":
        return analogous_colors(base_color)
    elif method == "акцент-аналогия":
        return accent_analogous_colors(base_color)
    elif method == "затемнение":
        return monochromatic_dark_colors(base_color)
    elif method == "засветление":
        return monochromatic_light_colors(base_color)
    elif method == "изображение":
        if not image_path:
            raise ValueError("Для метода 'Изображение' необходимо указать image_path.")
        return generate_palette_from_image(image_path)
    else:
        raise ValueError(f"Неизвестный метод: {method}")
