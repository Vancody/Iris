import unittest
import sys
import os
import colorsys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from methods import complementary_colors, triadic_colors, analogous_colors, monochromatic_dark_colors, monochromatic_light_colors, accent_analogous_colors, tetrad_colors

class TestMethods(unittest.TestCase):

    def test_complementary_colors(self):
        base_color = (100, 150, 200)
        result = complementary_colors(base_color)
        expected = ((100, 150, 200), (200, 150, 100))  # Пересчитанные значения
        self.assertEqual(result, expected)

    def test_triadic_colors(self):
        base_color = (100, 150, 200)
        result = triadic_colors(base_color)
        expected = ((100, 150, 200), (200, 100, 150), (150, 200, 100))  # Пересчитанные значения
        self.assertEqual(result, expected)

    def test_analogous_colors(self):
        base_color = (100, 150, 200)
        result = analogous_colors(base_color)
        expected = ((100, 150, 200), (100, 100, 200), (100, 200, 200))  # Пересчитанные значения
        self.assertEqual(result, expected)

    def test_monochromatic_dark_colors(self):
        base_color = (100, 150, 200)
        result = monochromatic_dark_colors(base_color)
        expected = ((100, 150, 200), (40, 60, 80), (30, 44, 60), (20, 30, 40), (10, 15, 20), (5, 7, 10))  # Пересчитанные значения
        self.assertEqual(result, expected)

    def test_monochromatic_light_colors(self):
        base_color = (100, 150, 200)
        result = monochromatic_light_colors(base_color)
        expected = ((100, 150, 200), (122, 166, 211), (146, 184, 222), (172, 202, 233), (200, 222, 243), (229, 242, 255))  # Пересчитанные значения
        self.assertEqual(result, expected)

    def test_accent_analogous_colors(self):
        base_color = (100, 150, 200)
        result = accent_analogous_colors(base_color)
        expected = ((100, 150, 200), (100, 100, 200), (150, 100, 200), (150, 200, 100))  # Пересчитанные значения
        self.assertEqual(result, expected)

    def test_tetrad_colors(self):
        base_color = (100, 150, 200)
        result = tetrad_colors(base_color)
        expected = ((100, 150, 200), (200, 100, 200), (200, 150, 100), (100, 200, 100))  # Пересчитанные значения
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
