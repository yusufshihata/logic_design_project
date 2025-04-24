import customtkinter as ctk
import tkinter as tk
from app.widgets import StyledButton, StyledEntry
from tkinter import ttk, messagebox


class ResultPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#121212")
        self.controller = controller

        StyledButton(self, text="Back to Calculator",
                     command=lambda: controller.show_frame("CalculationPage")).pack()


        table_frame = tk.Frame(self, bg="#121212")
        table_frame.pack(expand=True, fill="both", padx=20, pady=10)

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

        self.tree = ttk.Treeview(table_frame)
        self.tree.pack(side="left", expand=True, fill="both")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.tag_configure('evenrow', background='#212121')
        self.tree.tag_configure('oddrow', background='#2D2D2D')

    def update_results(self, syms, combs, results):
        self.tree.delete(*self.tree.get_children())
        columns = list(syms) + ["Result"]
        self.tree["columns"] = columns
        self.tree.column("#0", width=0, stretch=tk.NO)

        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, anchor=tk.CENTER, width=100, stretch=tk.YES)

        for i in range(combs.shape[1]):
            row_values = list(combs[:, i]) + [results[i]]
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", tk.END, values=row_values, tags=(tag,))