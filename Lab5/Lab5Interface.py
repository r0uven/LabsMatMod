import tkinter as tk
from tkinter import ttk, Frame

from Lab5.LogicFor5Lab import testingHypothesisOfVariancesEquality


class lab5ClassInterface(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Метка для отображения проверки гипотезы
        self.res_testingTheHypothesis = tk.Label(self, font=("Arial", 16))
        self.res_testingTheHypothesis.pack(pady=20)
        self.on_initialize()



    def on_initialize(self):
        self.res_testingTheHypothesis.config(text=testingHypothesisOfVariancesEquality())

