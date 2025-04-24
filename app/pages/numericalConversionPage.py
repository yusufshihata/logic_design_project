import numpy as np
import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry
from app.pages.tutorialPage import TutorialPage


class NumericalSystemConversionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        # Center container
        container = ctk.CTkFrame(self, fg_color="#121212")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        self.title_label = ctk.CTkLabel(
            container, text="Numerical System Conversion", font=("Arial", 16, "bold"), text_color="white"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # From system selection
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

        # To system selection
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

        # Number input
        self.number_label = ctk.CTkLabel(
            container, text="Number:", text_color="white"
        )
        self.number_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.number_entry = StyledEntry(container)
        self.number_entry.grid(row=3, column=1, padx=10, pady=5)

        # Convert button
        self.convert_button = StyledButton(
            container, text="Convert", command=self.perform_conversion
        )
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=15, padx=10)

        # Result display
        self.result_label = ctk.CTkLabel(
            container, text="Result: ", text_color="white"
        )
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

        # Back button
        StyledButton(container, text="Back",
                     command=lambda: controller.show_frame("MainPage")).grid(row=6, column=0, columnspan=2)

    def perform_conversion(self):
        pass  # Performs the numerical system conversion
