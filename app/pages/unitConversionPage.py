import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry

class MeasurementUnitConversionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        # Center container
        container = ctk.CTkFrame(self, fg_color="#121212")
        container.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        self.title_label = ctk.CTkLabel(
            container, text="Measurement Unit Conversion", font=("Arial", 16, "bold"), text_color="white"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Measurement type selection
        self.measurement_type_label = ctk.CTkLabel(
            container, text="Measurement Type:", text_color="white"
        )
        self.measurement_type_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.measurement_type_var = ctk.StringVar(value="Length")
        self.measurement_type_combobox = ctk.CTkComboBox(
            container, variable=self.measurement_type_var,
            values=["Length", "Weight", "Temperature"]
        )
        self.measurement_type_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.measurement_type_var.trace_add("write", self.update_unit_dropdowns)

        # From unit selection
        self.from_unit_label = ctk.CTkLabel(
            container, text="From Unit:", text_color="white"
        )
        self.from_unit_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.from_unit_var = ctk.StringVar()
        self.from_unit_combobox = ctk.CTkComboBox(
            container, variable=self.from_unit_var
        )
        self.from_unit_combobox.grid(row=2, column=1, padx=10, pady=5)

        # To unit selection
        self.to_unit_label = ctk.CTkLabel(
            container, text="To Unit:", text_color="white"
        )
        self.to_unit_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.to_unit_var = ctk.StringVar()
        self.to_unit_combobox = ctk.CTkComboBox(
            container, variable=self.to_unit_var
        )
        self.to_unit_combobox.grid(row=3, column=1, padx=10, pady=5)

        # Value input
        self.value_label = ctk.CTkLabel(
            container, text="Value:", text_color="white"
        )
        self.value_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.value_entry = StyledEntry(container)
        self.value_entry.grid(row=4, column=1, padx=10, pady=5)

        # Convert button
        self.convert_button = StyledButton(
            container, text="Convert", command=self.perform_conversion
        )
        self.convert_button.grid(row=5, column=0, columnspan=2, pady=15, padx=10)

        # Result display
        self.result_label = ctk.CTkLabel(
            container, text="Result: ", text_color="white"
        )
        self.result_label.grid(row=6, column=0, columnspan=2, pady=5, padx=10)

        # Back button
        StyledButton(container, text="Back",
                     command=lambda: controller.show_frame("MainPage")).grid(row=7, column=0, columnspan=2)

    def update_unit_dropdowns(self, *args):
        pass  # Updates unit options based on measurement type

    def perform_conversion(self):
        pass  # Performs the unit conversion
