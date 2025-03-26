import numpy as np
from sympy import symbols

def generate_combinations(n):
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

def print_truth_table(syms_list, combs, results):
    header = " | ".join(syms_list) + " | Output"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    for i in range(combs.shape[1]):
        row_values = [str(combs[j, i]) for j in range(combs.shape[0])]
        print(" | ".join(row_values) + f" | {int(results[i])}")
    print("-" * len(header))

def solve(syms):
    syms_list = syms.split(' ')
    n = len(syms_list)
    combs = generate_combinations(n)
    
    python_expr = input("The formula you need to calculate: ")
    results = []
    
    for i in range(combs.shape[1]):
        inputs = {k: v for k, v in zip(syms_list, combs[:, i].tolist())}
        result = eval(python_expr, {}, inputs)
        results.append(result)
    
    print_truth_table(syms_list, combs, results)

def tutorial():
    print("Welcome to our Boolean Algebra Calculator")
    print("-----------------------------------------")
    print("AND gate can be written as (and, &)")
    print("OR gate can be written as (or, |)")
    print("NOT gate can be written as (not)")
    print("XOR gate can be written as (^)")
    print("NAND, XNOR, NOR can be written as a combinations of AND, OR, and not")

tutorial()
symbols = input("Input your formula symbols: ")
solve(symbols)

