import tkinter as tk
from tkinter import ttk, Frame

from Lab1 import LogicFor1Lab
from Lab3 import LogicFor3Lab
from Lab4 import LogicFor4Lab


class lab4ClassInterface(ttk.Frame):
    def __init__(self, parent, controller, lab1=None, lab3=None):
        super().__init__(parent)
        self.lab1 = lab1
        self.lab3 = lab3

        # Метка для отображения проверки гипотезы по критерию пирсона
        self.res_testingTheHypothesis = tk.Label(self, font=("Arial", 16))
        self.res_testingTheHypothesis.pack(pady=20)

        #self.on_initialize()

    def on_initialize(self):
        valuesFrom1Lab = self.lab1.valuesFrom1Lab
        valuesFrom3Lab = self.lab3.valuesFrom3Lab
        valuesFrom4Lab = LogicFor4Lab.testingThePearsonHypothesis(valuesFrom1Lab, valuesFrom3Lab)
        self.res_testingTheHypothesis.config(text=f"Результат исследования = {valuesFrom4Lab}")
