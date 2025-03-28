import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import customtkinter as ctk
from app.screens import MainPage, ResultPage, TutorialPage

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class BooleanAlgebraCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Boolean Algebra Calculator")
        self.master.geometry("800x500")
        self.master.resizable(True, True)

        self.container = ctk.CTkFrame(master, fg_color="#121212")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (MainPage, ResultPage, TutorialPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def generate_combinations(self, n):
        num_combs = 2**n
        combs = np.ones((n, num_combs))
        for i in range(n):
            padding = num_combs // (2 ** (i + 1))
            idx = 0
            for j in range(0, num_combs, padding):
                if idx % 2 == 0:
                    combs[i, j:j+padding] = 0
                idx += 1
        return combs.astype(int)

def main():
    root = ctk.CTk()
    app = BooleanAlgebraCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

