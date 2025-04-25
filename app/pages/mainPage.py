import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from app.widgets import StyledButton, StyledEntry
import numpy as np

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        title = ctk.CTkLabel(self, text="Boolean Algebra Tools", font=("Poppins", 24, "bold"), text_color="#1E88E5")
        title.pack(pady=20)

        StyledButton(self, text="Boolean Algebra Calculator",
                     command=lambda: controller.show_frame("CalculationPage")).pack(pady=10)
        StyledButton(self, text="Storage Unit Conversion",
                     command=lambda: controller.show_frame("StorageUnitConversionPage")).pack(pady=10)
        StyledButton(self, text="Numerical System Conversion",
                     command=lambda: controller.show_frame("NumericalSystemConversionPage")).pack(pady=10)
