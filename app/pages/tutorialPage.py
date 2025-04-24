import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry


class TutorialPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        title = ctk.CTkLabel(
            self, 
            text="How to Use Boolean Algebra Calculator", 
            font=("Poppins", 24, "bold"), 
            text_color="#1E88E5"
        )
        title.pack(pady=20)

        tutorial_text = ctk.CTkTextbox(
            self, 
            width=600, 
            height=300, 
            font=("Courier", 10),
            fg_color="#212121",
            text_color="white",
            corner_radius=10
        )
        tutorial_text.pack(expand=True, fill="both", padx=40, pady=20)
        tutorial_text.insert(tk.END, 
            "Welcome to Boolean Algebra Calculator\n"
            "-----------------------------------------\n"
            "• AND gate can be written as (and, &)\n"
            "• OR gate can be written as (or, |)\n"
            "• NOT gate can be written as (not)\n"
            "• XOR gate can be written as (^)\n"
            "• NAND, XNOR, NOR can be written as combinations of AND, OR, and not\n\n"
            "Usage:\n"
            "1. Enter the variable names separated by spaces in the 'Add the variables' field.\n"
            "2. Type your Boolean formula using the variables in the 'Enter the formula' field.\n"
            "3. Click 'Calculate' to see the truth table results.\n"
            "4. Navigate back to this tutorial anytime by clicking on 'How does it work?'\n"
        )
        tutorial_text.configure(state="disabled")

        StyledButton(self, text="Back to Calculator",
                     command=lambda: controller.show_frame("CalculationPage")).pack()
