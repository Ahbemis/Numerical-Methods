import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
# read_data = np.loadtxt('data.txt')
# t = read_data[:, 0]
# x = read_data[:, 1]
# plt.figure(figsize=(6, 5))
# plt.plot(t, x, label='x(t) real', color = 'b', linestyle='--')
# plt.xlabel('Time (t)')
# plt.ylabel('Value')
# plt.title('Position vs Time (Real)')
# plt.legend()
# plt.grid('on')
# plt.show()


# Define the function
def f(x):
    return np.cosh(x) * np.cos(x) + 1

# Initial guess for the roots
initial_guesses = np.linspace(-10, 10, 100)

# Find the roots
roots = []
for guess in initial_guesses:
    root = fsolve(f, guess)[0]
    root = round(root, 2)
    if np.isclose(f(root), 0, atol=10) and root not in roots:
        roots.append(root)

print("Roots of the function are:", roots)

