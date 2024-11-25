import tkinter as tk
from tkinter import ttk

from Lab6.LogicFor6Lab import correlationAnalysis


class lab6ClassInterface(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Метка для отображения проверки гипотезы
        self.res_correlationAnalysis = tk.Label(self, font=("Arial", 16))
        self.res_correlationAnalysis.pack(pady=20)



    def on_initialize(self):
        self.res_correlationAnalysis.config(text=correlationAnalysis())

