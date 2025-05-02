import numpy as np
import matplotlib.pyplot as plt

# Define the time array
t = np.linspace(0, 10, 100)

# Define the position function x(t)
x = 5*t**3 + 2*t**2 -7

# Compute the velocity v(t) = dx/dt using numpy's gradient function
v = np.gradient(x, t)
vr = 15*t**2 + 4*t
# Compute the acceleration a(t) = d^2x/dt^2 using numpy's gradient function
a = np.gradient(v, t)
ar = 30*t + 4
# Plot the position, velocity, and acceleration on the same plot
plt.figure(figsize=(6, 5))

plt.plot(t, x, label='x(t)')
plt.plot(t, v, label='v(t)', color='r')
plt.plot(t, a, label='a(t)', color='g')
plt.xlabel('Time (t)')
plt.ylabel('Value')
plt.title('Position, Velocity, and Acceleration vs Time (Simulated)')
plt.legend()
plt.grid('on')
plt.figure(figsize=(6, 5))
plt.plot(t, x, label='x(t) real', color = 'b', linestyle='--')
plt.plot(t, vr, label='v(t) real', color='r', linestyle='--')
plt.plot(t, ar, label='a(t) real', color='g', linestyle='--')

plt.xlabel('Time (t)')
plt.ylabel('Value')
plt.title('Position, Velocity, and Acceleration vs Time (Real)')
plt.legend()
plt.grid('on')

plt.tight_layout()
plt.show()
