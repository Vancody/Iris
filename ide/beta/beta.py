import tkinter as tk
from tkinter import colorchooser, filedialog, Label, ttk
from PIL import ImageTk, Image, ImageDraw
from colorthief import ColorThief
import random
import colorsys

class ColorPaletteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Iris - Генератор цветовых палитр")
        self.master.configure(bg="#333333")
        self.master.wm_iconbitmap("icon.ico")

        # Загружаем изображение для фона
        background_image = Image.open("bg.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Создаем метку с фоновым изображением
        self.background_label = tk.Label(self.master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создаем рамку для выбора цвета и метода сочетания цветов
        self.control_frame = tk.Frame(self.master, bg="#333333")
        self.control_frame.pack(side=tk.TOP, pady=10)

        # Создаем список выбора метода сочетания цветов
        self.method_options = ["Выберите метод сочетания", "Комплиментарность", "Триада", "Тетрада", "Аналогия", "Акцент-аналогия", "Затемнение", "Засветление", "Изображение"]
        self.method_choice = tk.StringVar()
        self.method_choice.set(self.method_options[0])
        self.method_menu = tk.OptionMenu(self.control_frame, self.method_choice, *self.method_options[1:], command=self.update_visibility)
        self.method_menu.config(bg="#949494", fg="white")
        self.method_menu.pack(side=tk.LEFT, padx=5)

        # Создаем кнопку для выбора цвета
        self.choose_color_button = tk.Button(self.control_frame, text="Выбрать цвет", command=self.choose_color, bg="#949494", fg="white", state=tk.DISABLED) 
        self.choose_color_button.pack(side=tk.LEFT, padx=5)

        # Создаем кнопку для загрузки изображения
        self.load_image_button = tk.Button(self.control_frame, text="Импортировать", command=self.load_image, bg="#949494", fg="white")
        self.load_image_button.pack(side=tk.LEFT, padx=5)
        self.load_image_button.pack_forget()  # Скрываем кнопку

        # Создаем кнопку для выбора случайного цвета
        self.random_color_button = tk.Button(self.control_frame, text="Случайный цвет", command=self.random_color, bg="#949494", fg="white")
        self.random_color_button.pack(side=tk.LEFT, padx=5)
        self.random_color_button.pack_forget()  # Скрываем кнопку

        # Создаем рамку для отображения палитры
        self.palette_frame = tk.Frame(self.master, bg="#333333")
        self.palette_frame.pack(side=tk.TOP, pady=10)        

        # Создаем Canvas для отображения палитры
        self.palette_canvas = tk.Canvas(self.palette_frame, width=500, height=150, bg="#333333", highlightthickness=0) 
        self.palette_canvas.pack()

        # Создаем кнопку для сохранения палитры
        self.save_palette_button = tk.Button(self.master, text="Сохранить палитру", command=self.save_palette, bg="#949494", fg="white")
        self.save_palette_button.pack(side=tk.BOTTOM, pady=10)

        self.palette = None
        self.image_filename = None
        
    #Методы сочетаний
    def complementary_colors(self, base_color): # Комплементарность
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        complementary_hue = (base_hue + 0.5) % 1.0
        complementary_rgb = colorsys.hsv_to_rgb(complementary_hue, base_saturation, base_value)
        return base_color, tuple(int(x * 255) for x in complementary_rgb)

    def triadic_colors(self, base_color): # Триада
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        first_triad_hue = (base_hue + 1/3) % 1.0
        second_triad_hue = (base_hue + 2/3) % 1.0
        first_triad_rgb = colorsys.hsv_to_rgb(first_triad_hue, base_saturation, base_value)
        second_triad_rgb = colorsys.hsv_to_rgb(second_triad_hue, base_saturation, base_value)
        return base_color, tuple(int(x * 255) for x in first_triad_rgb), tuple(int(x * 255) for x in second_triad_rgb)

    def analogous_colors(self, base_color): # Аналогия
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        first_analogous_hue = (base_hue + 1/12) % 1.0
        second_analogous_hue = (base_hue - 1/12) % 1.0
        first_analogous_rgb = colorsys.hsv_to_rgb(first_analogous_hue, base_saturation, base_value)
        second_analogous_rgb = colorsys.hsv_to_rgb(second_analogous_hue, base_saturation, base_value)
        return base_color, tuple(int(x * 255) for x in first_analogous_rgb), tuple(int(x * 255) for x in second_analogous_rgb)

    def monochromatic_dark_colors(self, base_color): # Монохромность (тёмная)
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        return base_color, tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.4)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.3)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.2)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.1)), tuple(int(x * 255) for x in colorsys.hsv_to_rgb(base_hue, base_saturation, base_value * 0.05))

    def monochromatic_light_colors(self, base_color): # Монохромность (светлая)
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        white_value = 1.0  # Значение яркости для белого цвета
        num_steps = 6  # Количество шагов между исходным цветом и белым
        difference = white_value - base_value  # Разница между исходным цветом и белым
        step_size = difference / (num_steps - 1)  # Размер шага для равномерного распределения разницы

        light_colors = []
        for i in range(num_steps):
            light_value = base_value + step_size * i  # Вычисляем значение яркости для каждого шага
            light_saturation = base_saturation - (base_saturation * 0.16 * i)  # Убавляем насыщенность на 16% для каждого шага
            light_colors.append(tuple(min(255, int(x * 255)) for x in colorsys.hsv_to_rgb(base_hue, light_saturation, light_value)))

        return tuple(light_colors)


        
    def accent_analogous_colors(self, base_color): # Акцент-аналогия
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        analogous_hue = (base_hue + 1/12) % 1.0
        accent_hue = (base_hue + 1/6) % 1.0
        analogous_rgb = colorsys.hsv_to_rgb(analogous_hue, base_saturation, base_value)
        accent_rgb = colorsys.hsv_to_rgb(accent_hue, base_saturation, base_value)
        complementary_hue = (accent_hue + 0.5) % 1.0  # Генерируем комплиментарный цвет для второго цвета
        complementary_rgb = colorsys.hsv_to_rgb(complementary_hue, base_saturation, base_value)
        return base_color, tuple(int(x * 255) for x in analogous_rgb), tuple(int(x * 255) for x in accent_rgb), tuple(int(x * 255) for x in complementary_rgb)  # Возвращаем комплиментарный цвет

    def tetrad_colors(self, base_color): # Тетрада
        base_hue, base_saturation, base_value = colorsys.rgb_to_hsv(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        first_tetrad_hue = (base_hue + 1/4) % 1.0
        second_tetrad_hue = (base_hue + 2/4) % 1.0
        third_tetrad_hue = (base_hue + 3/4) % 1.0  # Добавляем третий цвет
        first_tetrad_rgb = colorsys.hsv_to_rgb(first_tetrad_hue, base_saturation, base_value)
        second_tetrad_rgb = colorsys.hsv_to_rgb(second_tetrad_hue, base_saturation, base_value)
        third_tetrad_rgb = colorsys.hsv_to_rgb(third_tetrad_hue, base_saturation, base_value)  # Генерируем третий цвет
        return base_color, tuple(int(x * 255) for x in first_tetrad_rgb), tuple(int(x * 255) for x in second_tetrad_rgb), tuple(int(x * 255) for x in third_tetrad_rgb)  # Возвращаем третий цвет

    def generate_palette_from_image(self, filename): # Генерация палитры из картинки
        color_thief = ColorThief(filename)
        colors = color_thief.get_palette(color_count=6)  # Получаем палитру из изображения
        return colors

    def choose_color(self): # Ручной выбор цвета
        color = colorchooser.askcolor(title="Выберите цвет") # Открываем диалог выбора цвета
        if color[1]:
            base_color = color[0] # Получаем выбранный цвет
            self.palette = self.generate_palette(base_color, self.method_choice.get()) # Генерируем палитру
            self.draw_palette() # Рисуем палитру

    def random_color(self): # Рандомный выбор цвета
        base_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.palette = self.generate_palette(base_color, self.method_choice.get())  # Генерируем палитру в соответствии с выбранным методом
        self.draw_palette()  # Рисуем палитру

    def draw_palette(self): # Отрисовка палитры на интерфейсе
        self.palette_canvas.delete("all") # Очищаем Canvas
        if self.palette:
            x = 15
            for color in self.palette: # Оформление
                self.palette_canvas.create_rectangle(x, 15, x + 70, 90, fill=f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}', outline="")
                self.palette_canvas.create_text(x + 35, 100, text=f'RGB: {color}', fill="white", font=("Helvetica", 6, "bold"))
                self.palette_canvas.create_text(x + 35, 120, text=f'HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}', fill="white", font=("Helvetica", 8, "bold"))
                x += 80

    def save_palette(self): # Экспортирование палитры как картинки
        if self.palette:
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]) # Запрашиваем у пользователя имя файла для сохранения
            if filename:
                img = Image.new('RGB', (590, 150), color='#333333')
                draw = ImageDraw.Draw(img)
                x = 15
                for color in self.palette: # Оформление
                    draw.rectangle([x, 15, x + 85, 100], fill=color)
                    draw.text((x, 105), f'RGB: {color}', fill="white")
                    draw.text((x, 125), f'HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}', fill="white")
                    x += 95
                img.save(filename) # Сохраняем изображение с палитрой

    def load_image(self): # Выбор изображения для создания палитры
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")]) # Открываем диалог выбора файла
        if filename: # Если пользователь выбрал файл
            self.image_filename = filename
            self.palette = self.generate_palette_from_image(filename)  # Создаем палитру из изображения
            self.draw_palette() # Рисуем палитру
            
    def update_visibility(self, event=None): #
        method = self.method_choice.get()
        if method == "Изображение":
            self.load_image_button.pack(side=tk.LEFT, padx=5)
            self.choose_color_button.config(state=tk.DISABLED)  # Делаем кнопку выбора цвета неактивной
            self.random_color_button.pack_forget()
        else:
            self.load_image_button.pack_forget()
            self.choose_color_button.config(state=tk.NORMAL)  # Возвращаем кнопке выбора цвета нормальное состояние
            self.random_color_button.pack(side=tk.LEFT, padx=5)
            
    def generate_palette(self, base_color, method): # Проверка выбранного метода 
        if method == "Комплиментарность":
            return self.complementary_colors(base_color)
        elif method == "Триада":
            return self.triadic_colors(base_color)
        elif method == "Тетрада":
            return self.tetrad_colors(base_color)
        elif method == "Аналогия":
            return self.analogous_colors(base_color)
        elif method == "Затемнение":
            return self.monochromatic_dark_colors(base_color)
        elif method == "Засветление":
            return self.monochromatic_light_colors(base_color)
        elif method == "Акцент-аналогия":
            return self.accent_analogous_colors(base_color)
        elif method == "Изображение":
            return self.generate_palette_from_image(self.image_filename)
        else:
            return []

def main(): # Запуск программы
    root = tk.Tk()
    root.resizable(False, False)  # Заблокировать изменение размера окна
    
    app = ColorPaletteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
