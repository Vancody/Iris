import sys
import os
from tkinter import filedialog
from PIL import Image, ImageDraw

# Добавляем директорию src в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def save_palette(palette, test_mode=False, test_filename="palette.png"):
    if palette:
        if test_mode:
            filename = test_filename
        else:
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        
        if filename:
            img = Image.new('RGB', (590, 150), color='#333333')
            draw = ImageDraw.Draw(img)
            x = 15
            for color in palette:
                draw.rectangle([x, 15, x + 85, 100], fill=color)
                draw.text((x, 105), f'RGB: {color}', fill="white")
                draw.text((x, 125), f'HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}', fill="white")
                x += 95
            img.save(filename)
            return True  # Возвращаем True при успешном сохранении
    return False 
