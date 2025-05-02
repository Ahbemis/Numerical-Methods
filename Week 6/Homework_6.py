import numpy as np
import math
def bisection_method(func, a, b, tol):
    iterations = 0
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None
    c = a
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iterations = iterations + 1
    return c, iterations

def false_position_method(func, a, b, tol):
    iteration = 0
    if func(a) * func(b) >= 0:
        print("False position method fails.")
        return None
    c = a
    while abs(func(c)) > tol:
        
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration = iteration + 1
    return c, iteration


if __name__ == "__main__":

    def func(x):
        return x**3 - 4*x + 1 

    a = 0
    b = 1
    tol = 1e-10
    if func(a) * func(b) >= 0:
        print("The initial interval does not bracket a root.")
    else:
        root_b = bisection_method(func, a, b, tol)
        if root_b is not None:
            print(f"The bisection root is: {root_b}")
        root_fp = false_position_method(func, a, b, tol)
        if root_fp is not None:
            print(f"The false position root is: {root_fp}")
        print(f"The Bisection method took {root_b[1]} tries")
        print(f"The False position method took {root_fp[1]} tries")