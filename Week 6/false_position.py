import numpy as np
import matplotlib.pyplot as plt
import math

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
            print('Root is in the left subinterval')
        else:
            a = c
            print('Root is in the right subinterval')
        iteration = iteration + 1    
        print(iteration)
    return c

if __name__ == "__main__":

    def func(x):
        return np.cosh(x) * np.cos(x) + 1

    a = 0
    b = math.pi
    tol = 0
    if func(a) * func(b) >= 0:
        print("The initial interval does not bracket a root.")
    else:
        root = false_position_method(func, a, b, tol)
        if root is not None:
            print(f"The root is: {root}")

        x = np.linspace(a, b, 100)

        plt.figure(figsize=(6, 5))
        plt.plot(x, func(x), label='Section of f(x)', color='b', linestyle='--')
        plt.plot(root, 0, 'ro', label=f'x ={root}')
        plt.grid('on')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('False Position Method')
        plt.show()
