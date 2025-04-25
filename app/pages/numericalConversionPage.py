import numpy as np
import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry


class NumericalSystemConversionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        container = ctk.CTkFrame(self, fg_color="#121212")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        self.title_label = ctk.CTkLabel(
            container, text="Numerical System Conversion", font=("Poppins", 16, "bold"), text_color="white"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.from_system_label = ctk.CTkLabel(
            container, text="From System:", text_color="white"
        )
        self.from_system_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.from_system_var = ctk.StringVar(value="Decimal")
        self.from_system_combobox = ctk.CTkComboBox(
            container, variable=self.from_system_var,
            values=["Binary", "Decimal", "Hexadecimal", "Octal"]
        )
        self.from_system_combobox.grid(row=1, column=1, padx=10, pady=5)

        self.to_system_label = ctk.CTkLabel(
            container, text="To System:", text_color="white"
        )
        self.to_system_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.to_system_var = ctk.StringVar(value="Binary")
        self.to_system_combobox = ctk.CTkComboBox(
            container, variable=self.to_system_var,
            values=["Binary", "Decimal", "Hexadecimal", "Octal"]
        )
        self.to_system_combobox.grid(row=2, column=1, padx=10, pady=5)

        self.number_label = ctk.CTkLabel(
            container, text="Number:", text_color="white"
        )
        self.number_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.number_entry = StyledEntry(container)
        self.number_entry.grid(row=3, column=1, padx=10, pady=5)

        self.convert_button = StyledButton(
            container, text="Convert", command=self.perform_conversion
        )
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=15, padx=10)

        self.result_label = ctk.CTkLabel(
            container, text="Result: ", text_color="white"
        )
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

        StyledButton(container, text="Back",
                     command=lambda: controller.show_frame("MainPage")).grid(row=6, column=0, columnspan=2)

    def get_data(self):
        from_system = self.from_system_var.get()
        to_system = self.to_system_var.get()
        number_str = self.number_entry.get()

        return (from_system, to_system, number_str)

    def perform_conversion(self):
        from_system, to_system, number_str = self.get_data()
