import tkinter as tk
from tkinter import ttk

from Lab7.LogicFor7Lab import generate_and_fit_model


class lab7ClassInterface(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Метка для отображения проверки гипотезы
        self.coefficient = tk.Label(self, font=("Arial", 16))
        self.coefficient.pack(pady=20)



    def on_initialize(self):
        self.coefficient.config(text=generate_and_fit_model())

