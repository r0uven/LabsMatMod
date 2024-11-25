import tkinter as tk
from Lab2 import LogicFor2Lab  # Импорт логики для лабораторной 2


# Класс интерфейса для лабораторной 2
class lab2ClassInterface(tk.Frame):
    def __init__(self, parent, controller, lab1=None):
        super().__init__(parent)
        self.lab1 = lab1

        # Контейнер для центрирования элементов интерфейса
        container = tk.Frame(self)
        container.pack(anchor=tk.CENTER, expand=True, pady=20)

        # Метка для отображения коэффициента асимметрии
        self.asymmetry_coefficient_label = tk.Label(container, font=("Arial", 21))
        self.asymmetry_coefficient_label.pack(pady=20)

        # Метка для отображения коэффициента эксцесса
        self.excess_label = tk.Label(container, font=("Arial", 21))
        self.excess_label.pack(pady=20)

        #self.on_initialize()

    def on_initialize(self):
        valuesFrom1Lab = self.lab1.valuesFrom1Lab
        # Инициализируем расчет характеристик сразу при создании интерфейса
        valuesFrom2Lab = LogicFor2Lab.calculation_of_characteristics_from_2_labs(valuesFrom1Lab)
        # Обновляем метки на интерфейсе с новыми значениями
        self.asymmetry_coefficient_label.config(text=f"Коэффициент асимметрии(A) = {valuesFrom2Lab['asymmetry_coefficient']:.5f}")
        self.excess_label.config(text=f"Эксцесс(E) =  {valuesFrom2Lab['excess']:.5f}")
