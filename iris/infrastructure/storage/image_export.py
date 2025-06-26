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

import os
from PIL import Image, ImageDraw, ImageFont
from iris.domain.services.color_rules import lighten_color_hsv, rgb_to_hsl

base_dir = os.path.dirname(__file__)
resources_dir = os.path.join(base_dir, '..', '..', '..', 'resources')

try:
        base_dir = os.path.dirname(__file__)
        font_path = os.path.join(base_dir, '..', '..', '..', 'resources', 'Helvetica.ttf')
        
        font_rgb = ImageFont.truetype(font_path, 9)
        font_hex = ImageFont.truetype(font_path, 12)
        font_hsl = ImageFont.truetype(font_path, 9)
except:
        font_rgb = ImageFont.load_default()
        font_hex = ImageFont.load_default()
        font_hsl = ImageFont.load_default()

def save_palette_to_image(filename: str, palette: list[tuple[int, int, int]], watermark_text: str = "Created with Iris"):
    width = 590
    height = 185
    img = Image.new('RGB', (width, height), color='#333333')
    draw = ImageDraw.Draw(img)
    x = 15
    y = 0
    
    for color in palette:
        lighter_color = lighten_color_hsv(color, 0.2)
        r, g, b = color
        h, s, l = rgb_to_hsl((r, g, b))
        draw.rectangle(
            [x, 15, x + 85, 100],
            fill=color,
            outline=lighter_color,
            width=2
        )
        draw.text((x, 105), f'RGB: {color}', fill="white", font=font_rgb)
        draw.text((x, 120), f'HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}', fill="white", font=font_hex)
        draw.text((x, 140), f'HSL: {h:.0f}°, {s:.0f}%, {l:.0f}%', fill="white", font=font_hsl)
        x += 95
        y += 1

    while y<6:
        draw.rectangle([x, 15, x + 85, 100], fill="#2C2C2C")
        
        try:
            logo_path = os.path.join(resources_dir, 'logo.png')
            logo = Image.open(logo_path)
            logo = logo.resize((75, 75), Image.LANCZOS)
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            
            # Прозрачный слой для логотипа
            alpha = logo.split()[3]
            new_alpha = alpha.point(lambda a: int(a * 0.7)) 
            logo.putalpha(new_alpha)
            
            # Позиции
            img.paste(logo, (x + 4, 20), logo)
        
        except Exception as e:
            print(f"Ошибка загрузки логотипа: {e}")
        x += 95
        y += 1
    
    # Шрифт
    try:
        font_path = os.path.join(resources_dir, 'OpenSans.ttf')
        font = ImageFont.truetype(font_path, 12)
    except:
        font = ImageFont.load_default()

    try:
        logo_path = os.path.join(resources_dir, 'main_logo.png')
        logo = Image.open(logo_path)
        logo = logo.resize((35, 35), Image.LANCZOS)
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Позиции
        img.paste(logo, (20, height - 35), logo)
        text_position = (65, height - 25)
    except Exception as e:
        print(f"Ошибка загрузки логотипа: {e}")
        try:
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_position = ((width - text_width) / 2, height - 25)
        except AttributeError:
            text_width, _ = draw.textsize(watermark_text, font=font)
            text_position = ((width - text_width) / 2, height - 25)

    draw.text(text_position, watermark_text, font=font, fill="#888888")
    img.save(filename)