import sys
import os
import tkinter as tk
from tkinter import colorchooser, filedialog, Label, ttk
from PIL import ImageTk, Image, ImageDraw
from colorthief import ColorThief
import random
import colorsys

# Добавляем директорию src в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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



class ColorPaletteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Iris - Генератор цветовых палитр")
        self.master.configure(bg="#333333")
        self.master.wm_iconbitmap("../extensions/icon.ico")

        # Загружаем изображение для фона
        background_image = Image.open("../extensions/bg.png")
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
        self.save_palette_button = tk.Button(self.master, text="Сохранить палитру", command=self.save_function, bg="#949494", fg="white")
        self.save_palette_button.pack(side=tk.BOTTOM, pady=10)

        self.palette = None
        self.image_filename = None

    def save_function(self):
        # Вызываем функцию save_palette и передаем текущую палитру
        if self.palette:
                    save_palette(self.palette)
        
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
            return complementary_colors(base_color)
        elif method == "Триада":
            return triadic_colors(base_color)
        elif method == "Тетрада":
            return tetrad_colors(base_color)
        elif method == "Аналогия":
            return analogous_colors(base_color)
        elif method == "Затемнение":
            return monochromatic_dark_colors(base_color)
        elif method == "Засветление":
            return monochromatic_light_colors(base_color)
        elif method == "Акцент-аналогия":
            return accent_analogous_colors(base_color)
        elif method == "Изображение":
            return generate_palette_from_image(self.image_filename)
        else:
            return []

    def load_image(self): # Выбор изображения для создания палитры
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")]) # Открываем диалог выбора файла
        if filename: # Если пользователь выбрал файл
            self.image_filename = filename
            self.palette = generate_palette_from_image(filename)  # Создаем палитру из изображения
            self.draw_palette() # Рисуем палитру
    
def main(): # Запуск программы
    root = tk.Tk()
    root.resizable(False, False)  # Заблокировать изменение размера окна
    
    app = ColorPaletteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
