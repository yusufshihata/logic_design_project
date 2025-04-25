import numpy as np
import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry
from app.pages.tutorialPage import TutorialPage
from app.pages.resultPage import ResultPage
from tkinter import ttk, messagebox

class CalculationPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        main_frame = ctk.CTkFrame(self, fg_color="#121212")
        main_frame.pack(expand=True, fill="both", padx=40, pady=40)

        self.title = ctk.CTkLabel(
            main_frame, 
            text="Boolean Algebra Calculator", 
            font=("Poppins", 24, "bold"), 
            text_color="#1E88E5"
        )
        self.title.pack(pady=(0, 20))

        self.subtitle = ctk.CTkLabel(
            main_frame, 
            text="How does it work?", 
            font=("Poppins", 14, "underline"), 
            text_color="white",
            cursor="hand2"
        )
        self.subtitle.pack(pady=(0, 20))
        self.subtitle.bind("<Button-1>", lambda e: controller.show_frame('TutorialPage'))

        variables_frame = ctk.CTkFrame(main_frame, fg_color="#121212")
        variables_frame.pack(fill="x", pady=(0, 10))
        self.variables_label = ctk.CTkLabel(
            variables_frame, 
            text="Add the variables", 
            font=("Poppins", 14),
            text_color="white"
        )
        self.variables_label.pack(anchor="w")
        self.variables_entry = StyledEntry(variables_frame, width=50)
        self.variables_entry.pack(fill="x", pady=(5, 0))

        formula_frame = ctk.CTkFrame(main_frame, fg_color="#121212")
        formula_frame.pack(fill="x", pady=(20, 10))
        self.formula_label = ctk.CTkLabel(
            formula_frame, 
            text="Enter the formula", 
            font=("Poppins", 14),
            text_color="white"
        )
        self.formula_label.pack(anchor="w")
        self.formula_entry = StyledEntry(formula_frame, width=50)
        self.formula_entry.pack(fill="x", pady=(5, 0))

        self.calculate_button = StyledButton(
            main_frame, 
            text="Calculate", 
            command=self.calculate,
            width=30
        )
        self.calculate_button.pack(pady=(30, 0))

        StyledButton(self, text="Back to Home",
                command=lambda: controller.show_frame("MainPage")).pack(pady=(30,0))

    def generate_combinations(self, n):
        num_combs = 2 ** n
        combs = np.ones((n, num_combs), dtype=int)
        for i in range(n):
            padding = num_combs // (2 ** (i + 1))
            idx = 0
            for j in range(0, num_combs, padding):
                if idx % 2 == 0:
                    combs[i, j:j + padding] = 0
                idx += 1
        return combs

    def calculate(self):
            try:
                syms_list = self.variables_entry.get().split()
                python_expr = self.formula_entry.get()

                if not syms_list or not python_expr:
                    messagebox.showerror("Error", "Please enter variables and formula")
                    return

                n = len(syms_list)
                combs = self.generate_combinations(n)

                results = []
                for i in range(combs.shape[1]):
                    inputs = {k: v for k, v in zip(syms_list, combs[:, i].tolist())}
                    result = int(eval(python_expr, {}, inputs))
                    results.append(result)

                result_page = self.controller.frames['ResultPage']
                result_page.update_results(syms_list, combs, results)
                self.controller.show_frame('ResultPage')
            except Exception as e:
                messagebox.showerror("Error", str(e))

