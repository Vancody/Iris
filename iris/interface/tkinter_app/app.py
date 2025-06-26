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

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import ImageTk, Image
import os
import random
import webbrowser 

from iris.application.generate_palette import generate_palette
from iris.infrastructure.storage.image_export import save_palette_to_image
from iris.domain.entities.palette import Palette
from iris.domain.services.color_rules import lighten_color_rgb, rgb_to_hsl
from iris.infrastructure.database.handler import create_connection, close_connection

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')

def check_database_connection() -> bool:
    try:
        conn = create_connection()
        if conn:
            close_connection(conn)
            return True
    except:
        pass
    return False

class ColorPaletteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Iris — Генератор цветовых палитр")
        self.master.configure(bg="#333333")

        # Ресурсы
        try:
            icon_path = os.path.join(os.path.join(RESOURCES_DIR, 'ico.ico'))
            self.master.wm_iconbitmap(icon_path)
        except Exception as e:
            print(f"Не удалось загрузить иконку: {e}")

        try:
            bg_path = os.path.join(RESOURCES_DIR, 'bg.png')
            background_image = Image.open(bg_path)
            self.background_photo = ImageTk.PhotoImage(background_image)
            self.background_label = tk.Label(self.master, image=self.background_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Не удалось загрузить фоновое изображение: {e}")
            self.master.configure(bg="#333333")

        # Элементы управления
        self.db_status_bar = tk.Label(self.master, text="База данных: проверка...", bg="#202020", fg="white", anchor="w")   
        self.db_status_bar.pack(side=tk.TOP, fill=tk.X, pady=(2, 3), padx=(5, 0))
        self.update_db_status()

        self.control_frame = tk.Frame(self.master, bg="#333333")
        self.control_frame.pack(side=tk.TOP, pady=10)
        

        self.method_options = [
            "Выберите метод сочетания",
            "Комплиментарность", "Триада", "Тетрада",
            "Аналогия", "Акцент-аналогия",
            "Затемнение", "Засветление",
            "Изображение"
        ]
        self.method_choice = tk.StringVar()
        self.method_choice.set(self.method_options[0])
        self.method_menu = tk.OptionMenu(self.control_frame, self.method_choice, *self.method_options[1:], command=self.update_visibility)
        self.method_menu.config(bg="#949494", fg="white",  font=("Arial", 9, "bold"), relief=tk.FLAT, borderwidth=0, indicatoron=0)
        self.method_menu.pack(side=tk.LEFT, padx=5)

        self.choose_color_button = tk.Button(self.control_frame, text="Выбрать цвет", command=self.choose_color, bg="#949494", fg="white",  font=("Arial", 9, "bold"), relief=tk.FLAT, borderwidth=0, padx=5, state=tk.DISABLED)
        self.choose_color_button.pack(side=tk.LEFT, padx=5)

        self.load_image_button = tk.Button(self.control_frame, text="Импортировать", command=self.load_image, bg="#949494", fg="white",  font=("Arial", 9, "bold"), relief=tk.FLAT, borderwidth=0, padx=5)
        self.load_image_button.pack(side=tk.LEFT, padx=5)
        self.load_image_button.pack_forget()

        self.random_color_button = tk.Button(self.control_frame, text="Случайный цвет", command=self.random_color, bg="#949494", fg="white",  font=("Arial", 9, "bold"), relief=tk.FLAT, borderwidth=0, padx=5)
        self.random_color_button.pack(side=tk.LEFT, padx=5)
        self.random_color_button.pack_forget()

        self.palette_frame = tk.Frame(self.master, bg="#333333")
        self.palette_frame.pack(side=tk.TOP, pady=10)

        self.palette_canvas = tk.Canvas(self.palette_frame, width=500, height=150, bg="#333333", highlightthickness=0)
        self.palette_canvas.pack()
        x = 15
        y = 0
        while y<6:
                self.palette_canvas.create_rectangle(x, 15, x + 70, 90, fill="#2C2C2C", outline="")
                x += 80
                y += 1
        
        # Подвал
        self.footer_frame = tk.Frame(self.master, bg="#202020")
        self.footer_frame.pack(side=tk.BOTTOM, pady=4, anchor="center")
        

        tk.Label(
            self.footer_frame, 
            text="Разработчик: Mitori Vancody Firelight", 
            bg="#202020", 
            fg="#888888", 
            font=("Arial", 8)
        ).pack(side=tk.LEFT, padx=(0, 8), pady=3)
        

        self.social_links = [
            {"name": "GitHub", "icon": "github_icon.png", "url": "https://github.com/Vancody"},
            {"name": "VK", "icon": "vk_icon.png", "url": "https://vk.com/mitori_territory"},
            {"name": "Telegram", "icon": "telegram_icon.png", "url": "https://t.me/Vancody_Firelight"}
        ]
        

        self.social_buttons = []
        for link in self.social_links:
            try:
                icon_path = os.path.join(RESOURCES_DIR, link["icon"])
                icon = Image.open(icon_path)
                icon = icon.resize((24, 24), Image.LANCZOS)
                photo = ImageTk.PhotoImage(icon)
                
                btn = tk.Button(
                    self.footer_frame,
                    image=photo,
                    bg="#202020",
                    relief=tk.FLAT,
                    command=lambda url=link["url"]: webbrowser.open(url)
                )
                btn.image = photo 
                btn.pack(side=tk.LEFT, padx=5)
                self.social_buttons.append(btn)
            except Exception as e:
                print(f"Не удалось загрузить иконку {link['name']}: {e}")
                tk.Button(
                    self.footer_frame,
                    text=link["name"],
                    bg="#333333",
                    fg="#888888",
                    relief=tk.FLAT,
                    command=lambda url=link["url"]: webbrowser.open(url)
                ).pack(side=tk.LEFT, padx=5)

        self.save_palette_button = tk.Button(self.master, text="Сохранить палитру", command=self.save_palette, bg="#949494", fg="white",  font=("Arial", 11, "bold"), relief=tk.FLAT, borderwidth=0, padx=5)
        self.save_palette_button.pack(side=tk.BOTTOM, pady=10)

        # Данные
        self.palette: Palette | None = None
        self.image_filename: str | None = None
    
    def update_db_status(self):
        connected = check_database_connection()
        if connected:
            self.db_status_bar.config(text="База данных: подключено ✔", fg="#00cc66")
        else:
            self.db_status_bar.config(text="База данных: ошибка подключения ✖", fg="#ff4444")

    def update_visibility(self, event=None):
        method = self.method_choice.get()
        if method == "Изображение":
            self.load_image_button.pack(side=tk.LEFT, padx=5)
            self.choose_color_button.config(state=tk.DISABLED)
            self.random_color_button.pack_forget()
        else:
            self.load_image_button.pack_forget()
            self.choose_color_button.config(state=tk.NORMAL)
            self.random_color_button.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет")[0]
        if color:
            base_color = tuple(map(int, color))
            self.generate_and_draw(base_color)

    def random_color(self):
        base_color = tuple(random.randint(0, 255) for _ in range(3))
        self.generate_and_draw(base_color)

    def load_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
        if filename:
            self.image_filename = filename
            self.generate_and_draw((0, 0, 0)) 

    def generate_and_draw(self, base_color: tuple[int, int, int]):
        method = self.method_choice.get()
        try:
            self.palette = generate_palette(base_color, method, image_path=self.image_filename)
            self.draw_palette()
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def draw_palette(self):
        self.palette_canvas.delete("all")
        if self.palette:
            x = 15
            y = 0
            for color in self.palette.to_rgb_list():
                r, g, b = color
                h, s, l = rgb_to_hsl((r, g, b))

                lr, lg, lb = lighten_color_rgb(color, 0.2)
                lighter_hex = f'#{lr:02x}{lg:02x}{lb:02x}'
                color_hex = f'#{r:02x}{g:02x}{b:02x}'
                rgb_text = f'({r}, {g}, {b})'
                hsl_text = f'{h:.0f}°, {s:.0f}%, {l:.0f}%'

                # Прямоугольник
                self.palette_canvas.create_rectangle(
                    x, 15, x + 70, 90,
                    fill=color_hex,
                    outline=lighter_hex,
                    width=2
                )

                # RGB
                rgb_id = self.palette_canvas.create_text(
                    x + 35, 100,
                    text=f'RGB: {rgb_text}',
                    fill="white",
                    font=("Helvetica", 6, "bold")
                )
                self.palette_canvas.tag_bind(rgb_id, "<Button-1>", lambda e, t=rgb_text: self.copy_to_clipboard(t))
                self.palette_canvas.tag_bind(rgb_id, "<Enter>", lambda e: self.show_tooltip(self.palette_canvas, "Нажмите, чтобы скопировать", e.x_root + 10, e.y_root + 10))
                self.palette_canvas.tag_bind(rgb_id, "<Leave>", self.hide_tooltip)

                # HEX
                hex_id = self.palette_canvas.create_text(
                    x + 35, 120,
                    text=f'HEX: {color_hex}',
                    fill="white",
                    font=("Helvetica", 8, "bold")
                )
                self.palette_canvas.tag_bind(hex_id, "<Button-1>", lambda e, t=color_hex: self.copy_to_clipboard(t))
                self.palette_canvas.tag_bind(hex_id, "<Enter>", lambda e: self.show_tooltip(self.palette_canvas, "Нажмите, чтобы скопировать", e.x_root + 10, e.y_root + 10))
                self.palette_canvas.tag_bind(hex_id, "<Leave>", self.hide_tooltip)

                # HSL
                hsl_id = self.palette_canvas.create_text(
                    x + 35, 140,
                    text=f'HSL: {hsl_text}',
                    fill="white",
                    font=("Helvetica", 6, "bold")
                )
                self.palette_canvas.tag_bind(hsl_id, "<Button-1>", lambda e, t=hsl_text: self.copy_to_clipboard(t))
                self.palette_canvas.tag_bind(hsl_id, "<Enter>", lambda e: self.show_tooltip(self.palette_canvas, "Нажмите, чтобы скопировать", e.x_root + 10, e.y_root + 10))
                self.palette_canvas.tag_bind(hsl_id, "<Leave>", self.hide_tooltip)

                x += 80
                y += 1

            while y<6:
                self.palette_canvas.create_rectangle(x, 15, x + 70, 90, fill="#2C2C2C", outline="")
                x += 80
                y += 1
            

    def save_palette(self):
        if not self.palette:
            return

        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            save_palette_to_image(filename, self.palette.to_rgb_list())
    
    def copy_to_clipboard(self, text: str):
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        self.master.update()
        self.show_temp_message(f"Скопировано: {text}")
    
    def show_temp_message(self, message: str, duration: int = 2000):
        toast = tk.Toplevel(self.master)
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)

        label = tk.Label(
            toast,
            text=message,
            bg="#222222",
            fg="white",
            padx=10,
            pady=0,
            font=("Helvetica", 8, "bold")
        )
        label.pack()

        self.master.update_idletasks()
        toast.update_idletasks()

        margin_x = 10 
        margin_y = 35

        master_x = self.master.winfo_x()
        master_y = self.master.winfo_y()
        master_width = self.master.winfo_width()

        toast_width = toast.winfo_reqwidth()
        x = master_x + master_width - toast_width - margin_x
        y = master_y + margin_y

        toast.geometry(f"+{x}+{y}")
        toast.after(duration, toast.destroy)

    def show_tooltip(self, widget, text, x, y):
        self.hide_tooltip()
        self.tooltip = tk.Toplevel(self.master)
        self.tooltip.overrideredirect(True)
        self.tooltip.attributes("-topmost", True)
        label = tk.Label(self.tooltip, text=text, bg="#333333", fg="white",
                        font=("Helvetica", 7), padx=4, pady=2, bd=1, relief="solid")
        label.pack()
        self.tooltip.geometry(f"+{x}+{y}")

    def hide_tooltip(self, event=None):
        if hasattr(self, "tooltip") and self.tooltip.winfo_exists():
            self.tooltip.destroy()



def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = ColorPaletteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()