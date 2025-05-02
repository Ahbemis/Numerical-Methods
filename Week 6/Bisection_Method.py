import numpy as np
import matplotlib.pyplot as plt

def bisection_method(func, a, b, tol):
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
    return c

if __name__ == "__main__":

    def func(x):
        return np.cosh(x) * np.cos(x) + 1

    a = float(input("Enter the left bound: "))
    b = float(input("Enter the right bound: "))
    tol = 1e-15
    if func(a) * func(b) >= 0:
        print("The initial interval does not bracket a root.")
    else:
        root = bisection_method(func, a, b, tol)
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
        plt.title('Bisection Method')
        plt.show()
