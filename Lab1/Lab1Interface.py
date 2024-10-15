import tkinter as tk
from tkinter import ttk, Frame
from tkinter.constants import CENTER

from PIL.ImageOps import expand

from Lab1 import LogicFor1Lab

class lab1ClassInterface(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Фреймы для основных частей графического интерфейса
        self.topStripe = Frame(self) # верхняя линия с кнопками и таблом отображения и полем для ввода
        self.topStripe.pack()

        self.inputFieldsAndButtons = Frame(self.topStripe)
        self.inputFieldsAndButtons.pack(side=tk.LEFT)

        self.displayFieldAndScrollbar = Frame(self.topStripe)
        self.displayFieldAndScrollbar.pack(side=tk.RIGHT, padx=(10, 0), pady=0)

        self.tableFrame = Frame(self)
        self.tableFrame.pack(fill="both")

        # Лейбл для отображения выборочной средней и оценки дисперсии
        self.additionalCharacteristics = tk.Label(self, font=('',30,))
        self.additionalCharacteristics.pack(anchor=tk.CENTER, expand=True)

        # Создаем Treeview для отображения таблицы
        self.table = ttk.Treeview(self.tableFrame, columns=("dummy",), show='headings', height=5)
        self.table.column("dummy", width=0, stretch=False)  # Скрываем начальный столбец

        # добавляем горизонтальную прокрутку для таблицы
        self.tableScrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.tableScrollbar.set)

        # Добавляем Treeview на окно
        self.tableScrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx = (10,10))
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx = (10,10))

        # Создаем поле для ввода
        self.entry = tk.Entry(self.inputFieldsAndButtons, font=("Arial", 16))
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Создаем кнопку для добавления чисел
        self.add_button = tk.Button(self.inputFieldsAndButtons, text="Добавить", command=self.on_add_action, font=("Arial", 16))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Кнопка для вычисления значений, построения графиков, в общем для основной логики приложения
        eval_button = tk.Button(self.inputFieldsAndButtons, text="Рассчитать", command=self.on_eval_click, font=("Arial", 16))
        eval_button.grid(row=0, column=2, padx=(10, 0), pady=10)


        # Создаем метку для отображения введенных цифр
        self.text_widget = tk.Text(self.displayFieldAndScrollbar, wrap="none", height=1, width=30)
        self.text_widget.pack(pady=0)

        # Создаем горизонтальный скролбар для метки введенных чисел
        self.scrollbarText = tk.Scrollbar(self.displayFieldAndScrollbar, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        self.scrollbarText.pack(side=tk.BOTTOM, fill=tk.X, pady=0)
        self.text_widget.configure(xscrollcommand=self.scrollbarText.set) # Привязываем скролбар к текстовому полю
        self.text_widget.config(state=tk.DISABLED) # Устанавливаем состояние текстового поля в DISABLED

        # Устанавливаем фокус на поле ввода при запуске приложения
        self.entry.focus_set()


    # функция добавления числа в различные переменные
    def on_add_action(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            LogicFor1Lab.randNumbersArray.append(float(user_input)) # записываем в переменную из файла логики введенные значения
            numbers_str = ', '.join("{:.2f}".format(num) for num in LogicFor1Lab.randNumbersArray)  # делаем красивую строчку для отображения введенных чисел

            # запись в текстовый файл
            self.text_widget.config(state=tk.NORMAL)  # Включаем редактирование
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, numbers_str)
            self.text_widget.config(state=tk.DISABLED)  # Выключаем редактирование

            self.entry.delete(0, tk.END)  # удаляем число, которое ввели чтобы оно не оставалось в поле ввода
            self.entry.focus_set()  # Устанавливаем фокус на поле ввода

            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(f"{float(user_input):.2f}, ")

    def on_enter_pressed(self, event):
        """Действие при нажатии клавиши Enter."""
        # Проверяем, активен ли данный фрейм (например, по какому-либо флагу)
        if self.winfo_ismapped():
            self.add_button.invoke()  # Симулирует нажатие кнопки

    # Функция для инициализации расчетов(все расчеты в файле LogicFor1Lab.py)
    def on_eval_click(self):
        LogicFor1Lab.evaluate_on_display(self.additionalCharacteristics, self.table)  # переход ко 2 файлу содержащему логику