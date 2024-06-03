from colorthief import ColorThief

def generate_palette_from_image(filename):
    color_thief = ColorThief(filename)
    colors = color_thief.get_palette(color_count=6)
    return colors
