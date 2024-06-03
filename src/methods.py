import colorsys

def complementary_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    complementary_hue = (base_hue + 0.5) % 1.0
    complementary_rgb = colorsys.hsv_to_rgb(complementary_hue, base_saturation, base_value)
    return base_color, tuple(int(x * 255) for x in complementary_rgb)

def triadic_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    first_triad_hue = (base_hue + 1/3) % 1.0
    second_triad_hue = (base_hue + 2/3) % 1.0
    first_triad_rgb = colorsys.hsv_to_rgb(first_triad_hue, base_saturation, base_value)
    second_triad_rgb = colorsys.hsv_to_rgb(second_triad_hue, base_saturation, base_value)
    return base_color, tuple(int(x * 255) for x in first_triad_rgb), tuple(int(x * 255) for x in second_triad_rgb)

def analogous_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    first_analogous_hue = (base_hue + 1/12) % 1.0
    second_analogous_hue = (base_hue - 1/12) % 1.0
    first_analogous_rgb = colorsys.hsv_to_rgb(first_analogous_hue, base_saturation, base_value)
    second_analogous_rgb = colorsys.hsv_to_rgb(second_analogous_hue, base_saturation, base_value)
    return base_color, tuple(int(x * 255) for x in first_analogous_rgb), tuple(int(x * 255) for x in second_analogous_rgb)

def monochromatic_dark_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    return base_color, tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.4)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.3)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.2)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.1)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.05))

def monochromatic_light_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    white_value = 1.0
    num_steps = 6
    difference = white_value - base_value
    step_size = difference / (num_steps - 1)

    light_colors = []
    for i in range(num_steps):
        light_value = base_value + step_size * i
        light_saturation = base_saturation - (base_saturation * 0.16 * i)
        light_colors.append(tuple(min(255, int(x * 255)) for x in colorsys.hsv_to_rgb(base_hue, light_saturation, light_value)))

    return tuple(light_colors)

def accent_analogous_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    analogous_hue = (base_hue + 1/12) % 1.0
    accent_hue = (base_hue + 1/6) % 1.0
    analogous_rgb = colorsys.hsv_to_rgb(analogous_hue, base_saturation, base_value)
    accent_rgb = colorsys.hsv_to_rgb(accent_hue, base_saturation, base_value)
    complementary_hue = (accent_hue + 0.5) % 1.0
    complementary_rgb = colorsys.hsv_to_rgb(complementary_hue, base_saturation, base_value)
    return base_color, tuple(int(x * 255) for x in analogous_rgb), tuple(int(x * 255) for x in accent_rgb), tuple(int(x * 255) for x in complementary_rgb)

def tetrad_colors(base_color):
    base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
    first_tetrad_hue = (base_hue + 1/4) % 1.0
    second_tetrad_hue = (base_hue + 2/4) % 1.0
    third_tetrad_hue = (base_hue + 3/4) % 1.0
    first_tetrad_rgb = colorsys.hsv_to_rgb(first_tetrad_hue, base_saturation, base_value)
    second_tetrad_rgb = colorsys.hsv_to_rgb(second_tetrad_hue, base_saturation, base_value)
    third_tetrad_rgb = colorsys.hsv_to_rgb(third_tetrad_hue, base_saturation, base_value)
    return base_color, tuple(int(x * 255) for x in first_tetrad_rgb), tuple(int(x * 255) for x in second_tetrad_rgb), tuple(int(x * 255) for x in third_tetrad_rgb)
