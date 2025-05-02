import numpy as np
import matplotlib.pyplot as plt

L = 2.0
n = 4
h = L / n
x = np.linspace(0, L, n + 1)
F = 100 * np.sin(np.pi * x / L)

# Trapezoidal Rule
W_trap = (h/2) * (F[0] + 2 * sum(F[1:-1]) + F[-1])

# Simpson’s Rule
W_simp = (h/3) * (F[0] + 4 * sum(F[1:-1:2]) + 2 * sum(F[2:-1:2]) + F[-1])

# Exact
W_exact = 400 / np.pi

# Output
print(f"Trapezoidal Rule: {W_trap:.2f} N")
print(f"Simpson's Rule: {W_simp:.2f} N")
print(f"Exact Value: {W_exact:.2f} N")

# Plot
x_plot = np.linspace(0, L, 100)
F_plot = 100 * np.sin(np.pi * x_plot / L)
plt.plot(x_plot, F_plot, label='F(x) = 100 sin(πx / L)')
plt.xlabel('x (m)')
plt.ylabel('F(x) (N)')
plt.title('Distributed Force on Beam')
plt.grid(True)
plt.legend()
plt.show()