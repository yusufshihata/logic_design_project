import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry

class StorageUnitConversionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        container = ctk.CTkFrame(self, fg_color="#121212")
        container.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = ctk.CTkLabel(
            container,
            text="Data Storage Unit Conversion",
            font=("Poppins", 16, "bold"),
            text_color="white"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.units = ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"]

        self.from_unit_label = ctk.CTkLabel(
            container,
            text="From Unit:",
            text_color="white"
        )
        self.from_unit_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.from_unit_var = ctk.StringVar(value=self.units[2])
        self.from_unit_combobox = ctk.CTkComboBox(
            container,
            variable=self.from_unit_var,
            values=self.units
        )
        self.from_unit_combobox.grid(row=1, column=1, padx=10, pady=5)

        self.to_unit_label = ctk.CTkLabel(
            container,
            text="To Unit:",
            text_color="white"
        )
        self.to_unit_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.to_unit_var = ctk.StringVar(value=self.units[3])
        self.to_unit_combobox = ctk.CTkComboBox(
            container,
            variable=self.to_unit_var,
            values=self.units
        )
        self.to_unit_combobox.grid(row=2, column=1, padx=10, pady=5)

        self.value_label = ctk.CTkLabel(
            container,
            text="Value:",
            text_color="white"
        )
        self.value_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.value_entry = StyledEntry(container, placeholder_text="Enter numeric value")
        self.value_entry.grid(row=3, column=1, padx=10, pady=5)

        self.convert_button = StyledButton(
            container,
            text="Convert",
            command=self.perform_conversion
        )
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=15, padx=10)

        self.result_label = ctk.CTkLabel(
            container,
            text="Result: ",
            text_color="white"
        )
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5, padx=10)

        StyledButton(
            container,
            text="Back",
            command=lambda: controller.show_frame("MainPage")
        ).grid(row=6, column=0, columnspan=2)

    def get_data(self):
        raw = self.value_entry.get()
        try:
            value = float(raw)
        except ValueError:
            self.result_label.configure(
                text="Result: Invalid input. Please enter a number."
            )
            return

        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()

        return (from_unit, to_unit, value)
    
    def perform_conversion(self):
        from_unit, to_unit, value = self.get_data()
        print(from_unit, to_unit, value)
