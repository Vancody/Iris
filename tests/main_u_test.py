import unittest
from tkinter import Tk
import os
import sys
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import ColorPaletteApp
from methods import (
    complementary_colors,
    triadic_colors,
    analogous_colors,
    monochromatic_dark_colors,
    monochromatic_light_colors,
    accent_analogous_colors,
    tetrad_colors,
)
from palette_save import save_palette
from image_method import generate_palette_from_image


class TestColorPaletteApp(unittest.TestCase):

    def test_complementary_colors(self):
        color = (255, 0, 0)
        result = complementary_colors(color)
        self.assertIsNotNone(result)

    def test_triadic_colors(self):
        color = (255, 0, 0)
        result = triadic_colors(color)
        self.assertIsNotNone(result)

    def test_analogous_colors(self):
        color = (255, 0, 0)
        result = analogous_colors(color)
        self.assertIsNotNone(result)

    def test_monochromatic_dark_colors(self):
        color = (255, 0, 0)
        result = monochromatic_dark_colors(color)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 6)  # Убедитесь, что это соответствует фактическому количеству возвращаемых цветов

    def test_monochromatic_light_colors(self):
        color = (255, 0, 0)
        result = monochromatic_light_colors(color)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 6)  # Убедитесь, что это соответствует фактическому количеству возвращаемых цветов

    def test_accent_analogous_colors(self):
        color = (255, 0, 0)
        result = accent_analogous_colors(color)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)  # Убедитесь, что это соответствует фактическому количеству возвращаемых цветов

    def test_tetrad_colors(self):
        color = (255, 0, 0)
        result = tetrad_colors(color)
        self.assertIsNotNone(result)

    def test_generate_palette_from_image(self):
        # Создаем временное изображение для теста
        temp_image_path = "temp_image.jpg"
        Image.new("RGB", (100, 100), (255, 0, 0)).save(temp_image_path)
        try:
            palette = generate_palette_from_image(temp_image_path)
            self.assertIsNotNone(palette)
        finally:
            os.remove(temp_image_path)

    def test_save_palette(self):
        palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        result = save_palette(palette, test_mode=True)
        self.assertTrue(result)
        self.assertTrue(os.path.exists("palette.png"))
        os.remove("palette.png")

    def test_app_creation(self):
        root = Tk()
        app = ColorPaletteApp(root)
        self.assertIsNotNone(app)

if __name__ == '__main__':
    unittest.main()
