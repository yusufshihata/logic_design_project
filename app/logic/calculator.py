import numpy as np
from tkinter import ttk, messagebox
from app.pages.resultPage import ResultPage


def generate_combinations(n):
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

def calculate(variables_entry, formula_entry, controller):
        try:
            syms_list = variables_entry.get().split()
            python_expr = formula_entry.get()

            if not syms_list or not python_expr:
                messagebox.showerror("Error", "Please enter variables and formula")
                return

            n = len(syms_list)
            combs = generate_combinations(n)

            results = []
            for i in range(combs.shape[1]):
                inputs = {k: v for k, v in zip(syms_list, combs[:, i].tolist())}
                result = int(eval(python_expr, {}, inputs))
                results.append(result)

            result_page = controller.frames['ResultPage']
            result_page.update_results(syms_list, combs, results)
            controller.show_frame('ResultPage')
        except Exception as e:
            messagebox.showerror("Error", str(e))

