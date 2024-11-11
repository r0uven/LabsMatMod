import tkinter as tk
from tkinter import ttk, Frame

from Lab1 import LogicFor1Lab
from Lab3 import LogicFor3Lab
from Lab4 import LogicFor4Lab


class lab4ClassInterface(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Метка для отображения проверки гипотезы по критерию пирсона
        self.res_testingTheHypothesis = tk.Label(self, font=("Arial", 16))
        self.res_testingTheHypothesis.pack(pady=20)
        self.on_initialize()

    def on_initialize(self):
        valuesFrom1Lab = LogicFor1Lab.calculation_of_characteristics_from_1_labs()
        valuesFrom3Lab = LogicFor3Lab.calculation_of_characteristics_from_3_labs(valuesFrom1Lab)
        valuesFrom4Lab = LogicFor4Lab.testingTheHypothesis(valuesFrom1Lab, valuesFrom3Lab)
        self.res_testingTheHypothesis.config(text=f"Результат исследования = {valuesFrom4Lab}")
