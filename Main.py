import tkinter as tk
from Lab1.Lab1Interface import lab1ClassInterface
from Lab2.Lab2Interface import lab2ClassInterface
from Lab3.Lab3Interface import lab3ClassInterface
from Lab4.Lab4Interface import lab4ClassInterface
from Lab5.Lab5Interface import lab5ClassInterface
from Lab6.Lab6Interface import lab6ClassInterface
from Lab7.Lab7Interface import lab7ClassInterface


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Приложение с меню для переключения интерфейсов")
        self.geometry("950x400")  # Размер окна

        # Создаем основную структуру окна с меню слева и контентом справа
        self.grid_columnconfigure(1, weight=1)  # Вторая колонка (интерфейс) растягивается
        self.grid_rowconfigure(0, weight=1)  # Первая строка (фреймы) растягивается

        # Создаем фрейм для меню слева
        menu_frame = tk.Frame(self, width=170, bg='lightgray')
        menu_frame.grid(row=0, column=0, sticky="ns", )

        # Создаем фрейм для контента (интерфейсов) справа
        content_frame = tk.Frame(self)
        content_frame.grid(row=0, column=1, sticky="nsew")
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        # Словарь для хранения фреймов
        self.frames = {}

        # Список классов и их параметров
        frame_configs = [
            {"class": lab1ClassInterface, "extra_params": []},
            {"class": lab2ClassInterface, "extra_params": ["lab1ClassInterface"]},
            {"class": lab3ClassInterface, "extra_params": ["lab1ClassInterface"]},
            {"class": lab4ClassInterface, "extra_params": ["lab1ClassInterface", "lab3ClassInterface"]},
            {"class": lab5ClassInterface, "extra_params": []},
            {"class": lab6ClassInterface, "extra_params": []},
            {"class": lab7ClassInterface, "extra_params": []},
        ]

        # Добавляем фреймы в словарь
        for config in frame_configs:
            cls = config["class"]
            extra_param_names = config["extra_params"]

            # Находим параметры по их именам
            extra_params = [self.frames[name] for name in extra_param_names]

            # Создаём фрейм, передавая параметры как список
            frame = cls(content_frame, self, *extra_params)

            # Сохраняем и размещаем
            self.frames[cls.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        # Кнопки для меню слева
        button_for_lab1 = tk.Button(menu_frame, text="Лабораторная №1", command=lambda: self.show_frame("lab1ClassInterface"))
        button_for_lab1.pack(pady=10, padx=10, fill="x")

        button_for_lab2 = tk.Button(menu_frame, text="Лабораторная №2", command=lambda: self.show_frame("lab2ClassInterface"))
        button_for_lab2.pack(pady=10, padx=10, fill="x")

        button_for_lab3 = tk.Button(menu_frame, text="Лабораторная №3", command=lambda: self.show_frame("lab3ClassInterface"))
        button_for_lab3.pack(pady=10, padx=10, fill="x")

        button_for_lab4 = tk.Button(menu_frame, text="Лабораторная №4", command=lambda: self.show_frame("lab4ClassInterface"))
        button_for_lab4.pack(pady=10, padx=10, fill="x")

        button_for_lab5 = tk.Button(menu_frame, text="Лабораторная №5", command=lambda: self.show_frame("lab5ClassInterface"))
        button_for_lab5.pack(pady=10, padx=10, fill="x")

        button_for_lab6 = tk.Button(menu_frame, text="Лабораторная №6", command=lambda: self.show_frame("lab6ClassInterface"))
        button_for_lab6.pack(pady=10, padx=10, fill="x")

        button_for_lab7 = tk.Button(menu_frame, text="Лабораторная №7", command=lambda: self.show_frame("lab7ClassInterface"))
        button_for_lab7.pack(pady=10, padx=10, fill="x")

        # Показываем начальный фрейм
        self.show_frame("lab1ClassInterface")

    def show_frame(self, frame_name):
        """Поднимает выбранный фрейм на передний план"""
        frame = self.frames[frame_name]
        frame.tkraise()

        if frame_name == "lab1ClassInterface":
            # Устанавливаем привязку клавиши Enter только для lab1
            self.unbind("<Return>")  # Сначала удаляем предыдущие привязки
            self.bind("<Return>", frame.on_enter_pressed) # Привязываем клавишу "Enter" к функции добавления чисел(on_add_click) через функцию обработки нажатия клавиши Enter
        # Вызываем on_initialize только для активного фрейма
        if hasattr(frame, 'on_initialize'):
            frame.on_initialize()

if __name__ == "__main__":
    app = App()
    app.mainloop()
