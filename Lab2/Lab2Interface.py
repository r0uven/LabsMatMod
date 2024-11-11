import tkinter as tk

from Lab1 import LogicFor1Lab
from Lab2 import LogicFor2Lab  # Импорт логики для лабораторной 2


# Класс интерфейса для лабораторной 2
class lab2ClassInterface(tk.Frame):
    def __init__(self, parent, controller):
        """
        Конструктор класса интерфейса для лабораторной 2.
        Создает метки для отображения коэффициентов и вызывает функцию для расчета.
        """
        super().__init__(parent)

        # Контейнер для центрирования элементов интерфейса
        container = tk.Frame(self)
        container.pack(anchor=tk.CENTER, expand=True, pady=20)

        # Метка для отображения коэффициента асимметрии
        self.asymmetry_coefficient_label = tk.Label(container, font=("Arial", 21))
        self.asymmetry_coefficient_label.pack(pady=20)

        # Метка для отображения коэффициента эксцесса
        self.excess_label = tk.Label(container, font=("Arial", 21))
        self.excess_label.pack(pady=20)

        self.on_initialize()

    def on_initialize(self):
        valuesFrom1Lab = LogicFor1Lab.calculation_of_characteristics_from_1_labs()  # переход к файлу содержащему методы вычисления нужных в этой лабе данных

        # Инициализируем расчет характеристик сразу при создании интерфейса
        valuesFrom2Lab = LogicFor2Lab.calculation_of_characteristics_from_2_labs(valuesFrom1Lab)
        # Обновляем метки на интерфейсе с новыми значениями
        self.asymmetry_coefficient_label.config(text=f"Коэффициент асимметрии(A) = {valuesFrom2Lab["asymmetry_coefficient"]:.5f}")
        self.excess_label.config(text=f"Эксцесс(E) =  {valuesFrom2Lab["excess"]:.5f}")
