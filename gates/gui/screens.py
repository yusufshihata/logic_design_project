import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from gui.widgets import StyledButton, StyledEntry

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        # Main Frame inside MainPage
        main_frame = ctk.CTkFrame(self, fg_color="#121212")
        main_frame.pack(expand=True, fill="both", padx=40, pady=40)

        # Title
        self.title = ctk.CTkLabel(
            main_frame, 
            text="Boolean Algebra Calculator", 
            font=("Poppins", 24, "bold"), 
            text_color="#1E88E5"
        )
        self.title.pack(pady=(0, 20))

        # Clickable Subtitle (navigates to Tutorial page)
        self.subtitle = ctk.CTkLabel(
            main_frame, 
            text="How does it work?", 
            font=("Poppins", 14, "underline"), 
            text_color="white",
            cursor="hand2"
        )
        self.subtitle.pack(pady=(0, 20))
        self.subtitle.bind("<Button-1>", lambda e: controller.show_frame(TutorialPage))

        # Variables Input Section
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

        # Formula Input Section
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

        # Calculate Button
        self.calculate_button = StyledButton(
            main_frame, 
            text="Calculate", 
            command=self.calculate,
            width=30
        )
        self.calculate_button.pack(pady=(30, 0))

    def calculate(self):
        try:
            # Get variables and formula
            syms_list = self.variables_entry.get().split()
            python_expr = self.formula_entry.get()

            if not syms_list or not python_expr:
                messagebox.showerror("Error", "Please enter variables and formula")
                return

            n = len(syms_list)
            combs = self.controller.generate_combinations(n)

            results = []
            for i in range(combs.shape[1]):
                inputs = {k: v for k, v in zip(syms_list, combs[:, i].tolist())}
                result = int(eval(python_expr, {}, inputs))
                results.append(result)

            # Pass data to ResultPage and show it
            result_page = self.controller.frames[ResultPage]
            result_page.update_results(syms_list, combs, results)
            self.controller.show_frame(ResultPage)
        except Exception as e:
            messagebox.showerror("Error", str(e))

class TutorialPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        # Title
        title = ctk.CTkLabel(
            self, 
            text="How to Use Boolean Algebra Calculator", 
            font=("Poppins", 24, "bold"), 
            text_color="#1E88E5"
        )
        title.pack(pady=20)

        # Tutorial Text Area (using CTkTextbox for a modern look)
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

        # Back button
        back_button = StyledButton(
            self, 
            text="Back to Main", 
            command=lambda: controller.show_frame(MainPage)
        )
        back_button.pack(pady=10)

class ResultPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        # Back button
        back_button = StyledButton(
            self, 
            text="Back to Main", 
            command=lambda: controller.show_frame(MainPage)
        )
        back_button.pack(pady=10)

        # Table frame (using a standard Frame for Treeview)
        table_frame = tk.Frame(self, bg="#121212")
        table_frame.pack(expand=True, fill="both", padx=20, pady=10)

        # Configure style for Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#212121",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#212121",
                        font=("Poppins", 12))
        style.configure("Treeview.Heading",
                        background="#1E88E5",
                        foreground="white",
                        font=("Poppins", 12, "bold"),
                        relief="flat")
        style.map("Treeview", background=[('selected', '#1565C0')])

        # Create Treeview widget with scrollbar
        self.tree = ttk.Treeview(table_frame)
        self.tree.pack(side="left", expand=True, fill="both")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configure alternating row colors
        self.tree.tag_configure('evenrow', background='#212121')
        self.tree.tag_configure('oddrow', background='#2D2D2D')

    def update_results(self, syms, combs, results):
        self.tree.delete(*self.tree.get_children())
        columns = list(syms) + ["Result"]
        self.tree["columns"] = columns
        self.tree.column("#0", width=0, stretch=tk.NO)  # Hide default column

        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, anchor=tk.CENTER, width=100, stretch=tk.YES)

        for i in range(combs.shape[1]):
            row_values = list(combs[:, i]) + [results[i]]
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", tk.END, values=row_values, tags=(tag,))

