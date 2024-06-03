import pytest
from tkinter import Tk
import os
import sys
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


def app():
    root = Tk()
    app = ColorPaletteApp(root)
    yield app
    root.destroy()


def test_complementary_colors(app):
    base_color = (255, 0, 0)
    palette = complementary_colors(base_color)
    assert len(palette) == 2


def test_triadic_colors(app):
    base_color = (255, 0, 0)
    palette = triadic_colors(base_color)
    assert len(palette) == 3


def test_tetrad_colors(app):
    base_color = (255, 0, 0)
    palette = tetrad_colors(base_color)
    assert len(palette) == 4


def test_analogous_colors(app):
    base_color = (255, 0, 0)
    palette = analogous_colors(base_color)
    assert len(palette) == 3


def test_monochromatic_dark_colors(app):
    base_color = (255, 0, 0)
    palette = monochromatic_dark_colors(base_color)
    assert len(palette) == 5


def test_monochromatic_light_colors(app):
    base_color = (255, 0, 0)
    palette = monochromatic_light_colors(base_color)
    assert len(palette) == 5


def test_accent_analogous_colors(app):
    base_color = (255, 0, 0)
    palette = accent_analogous_colors(base_color)
    assert len(palette) == 6


def test_generate_palette_from_image(app):
    palette = generate_palette_from_image("path_to_image.jpg")
    assert len(palette) > 0


def test_save_palette(app):
    palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    save_palette(palette)
    # Проверьте, что файл был создан
    assert os.path.exists("palette.png")


def test_choose_color(app):
    app.choose_color()
    assert app.palette is not None


def test_random_color(app):
    app.random_color()
    assert app.palette is not None


def test_load_image(app):
    app.load_image()
    assert app.image_filename is not None


def test_generate_palette(app):
    base_color = (255, 0, 0)
    method = "Комплиментарность"
    palette = app.generate_palette(base_color, method)
    assert len(palette) > 0
