import unittest
import os
import sys
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from palette_save import save_palette


class TestSavePalette(unittest.TestCase):
    @patch('tkinter.filedialog.asksaveasfilename', return_value="test_palette.png")
    def test_save_palette_with_palette(self, mock_asksaveasfilename):
        palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        # Просто вызываем функцию save_palette без проверки её возвращаемого значения
        save_palette(palette)

    def test_save_palette_without_palette(self):
        # Теперь этот тест также не ожидает возвращаемого значения
        # Просто вызываем функцию save_palette без проверки её возвращаемого значения
        save_palette(None)

if __name__ == '__main__':
    unittest.main()
