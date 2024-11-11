import tkinter as tk
from Lab1.Lab1Interface import lab1ClassInterface
from Lab2.Lab2Interface import lab2ClassInterface
from Lab3.Lab3Interface import lab3ClassInterface
from Lab4.Lab4Interface import lab4ClassInterface


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

        # Добавляем фреймы в словарь
        for F in (lab1ClassInterface, lab2ClassInterface, lab3ClassInterface, lab4ClassInterface):
            frame = F(content_frame, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Кнопки для меню слева
        button_for_lab1 = tk.Button(menu_frame, text="Лабораторная №1", command=lambda: self.show_frame("lab1ClassInterface"))
        button_for_lab1.pack(pady=10, padx=10, fill="x")

        button_for_lab2 = tk.Button(menu_frame, text="Лабораторная №2", command=lambda: self.show_frame("lab2ClassInterface"))
        button_for_lab2.pack(pady=10, padx=10, fill="x")

        button_for_lab3 = tk.Button(menu_frame, text="Лабораторная №3", command=lambda: self.show_frame("lab3ClassInterface"))
        button_for_lab3.pack(pady=10, padx=10, fill="x")

        button_for_lab3 = tk.Button(menu_frame, text="Лабораторная №4", command=lambda: self.show_frame("lab4ClassInterface"))
        button_for_lab3.pack(pady=10, padx=10, fill="x")

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
        self.frames["lab2ClassInterface"].on_initialize()
        self.frames["lab3ClassInterface"].on_initialize()


if __name__ == "__main__":
    app = App()
    app.mainloop()
