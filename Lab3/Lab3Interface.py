import tkinter as tk
from tkinter import ttk, Frame

from Lab1.LogicFor1Lab import add_to_table
from Lab1 import LogicFor1Lab
from Lab3 import LogicFor3Lab


# Класс интерфейса для лабораторной 3
class lab3ClassInterface(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.tableFrame = Frame(self)
        self.tableFrame.pack(fill="both")

        # Создаем Treeview для отображения таблицы
        self.table = ttk.Treeview(self.tableFrame, columns=("dummy",), show='headings', height=5)
        self.table.column("dummy", width=0, stretch=False)  # Скрываем начальный столбец

        # добавляем горизонтальную прокрутку для таблицы
        self.tableScrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.tableScrollbar.set)

        # Добавляем Treeview и его скроллбар на окно
        self.tableScrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=(10, 10))
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 10))
        self.on_initialize()



    def on_initialize(self):
        valuesFrom1Lab = LogicFor1Lab.calculation_of_characteristics_from_1_labs()  # переход к файлу содержащему методы вычисления нужных в этой лабе данных
        valuesFrom3Lab = LogicFor3Lab.calculation_of_characteristics_from_3_labs(valuesFrom1Lab)
        intervalBoundaries_ForTable = valuesFrom1Lab['intervalBoundaries_ForTable']
        theoreticalFrequenciesForTable = valuesFrom3Lab['theoreticalFrequenciesForTable']
        add_to_table(intervalBoundaries_ForTable, theoreticalFrequenciesForTable, len(theoreticalFrequenciesForTable), self.table)
