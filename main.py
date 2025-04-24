import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import numpy as np
from app.pages.calculationPage import CalculationPage
from app.pages.mainPage import MainPage
from app.pages.resultPage import ResultPage
from app.pages.tutorialPage import TutorialPage
from app.pages.unitConversionPage import MeasurementUnitConversionPage
from app.pages.numericalConversionPage import NumericalSystemConversionPage

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class BooleanAlgebraCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Boolean Algebra Calculator")
        self.master.geometry("800x500")
        self.master.resizable(True, True)

        container = ctk.CTkFrame(master, fg_color="#121212")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for PageClass in [
            MainPage,
            CalculationPage,
            ResultPage,
            TutorialPage,
            MeasurementUnitConversionPage,
            NumericalSystemConversionPage
        ]:
            name = PageClass.__name__
            frame = PageClass(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name: str):
        self.frames[page_name].tkraise()

    def generate_combinations(self, n: int):
        num_combs = 2 ** n
        combs = [[(i >> bit) & 1 for i in range(num_combs)] for bit in reversed(range(n))]
        return np.array(combs, dtype=int)

def main():
    root = ctk.CTk()
    app = BooleanAlgebraCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
