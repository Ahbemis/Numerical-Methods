# ODE.py
# Solving an Ordinary Differential Equation (ODE) using Euler's Method
import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t0, t_end, h):
    """
    Solves an ODE using Euler's method.

    Parameters:
        f: Function representing dy/dt = f(t, y), the derivative of y with respect to t
        y0: Initial value of y at t = t0
        t0: Initial time
        t_end: End time for the solution
        h: Step size for the numerical approximation

    Returns:
        t_values: List of time values where the solution is approximated
        y_values: List of corresponding y values at each time step
    """
    # Initialize lists to store time and solution values
    t_values = [t0]
    y_values = [y0]

    # Initialize current time and solution value
    t = t0
    y = y0

    # # Perform Euler's method until the end time is reached
    # while t < t_end:
    #     # Update y using the Euler formula: y_next = y_current + h * f(t, y)
    #     y = y + 0.5*h * f(t, y)
    #     y2 = y + h * f(t + 0.5*h, y)
    #     # Increment time by the step size
    #     t = t + h
    #     # Append the new time and solution values to the lists
    #     t_values.append(t)
    #     y_values.append(y)

    while t < t_end:
        y_values = h * f(t, y)
        y2_values = h * f(t + h, y + y_values)
        
        t = t + h
        t_values.append(t)
    # Return the computed time and solution values
        return t_values, y_values, y2_values


# Example usage
if __name__ == "__main__":
    # Define the ODE dy/dt = 6y^2 - 10y + 3
    def f(t, y):
        return 6 * y**2 - 10 * y + 3

    # Initial conditions
    y0 = 1  # Initial value of y
    t0 = 0  # Initial time
    t_end = 5  # End time for the solution
    h = 0.01  # Step size for the numerical approximation   

    # Solve the ODE using Euler's method
    t_values, y_values, y2_values = euler_method(f, y0, t0, t_end, h)

    # Print the results in a tabular format
    for t, y in zip(t_values, y_values, y2_values):
        print(f"t = {t:.2f}, y = {y:.4f}")

    # Plotting the results
    plt.plot(t_values, y_values, label="Euler Method")
    plt.plot(t_values, np.exp(-2 * np.array(t_values)), label="Data Points")
    plt.plot(t_values, y2_values, 'ro', label="Data Points")
    plt.title("Euler's Method for ODE")
    plt.legend()
    plt.grid()
    plt.xlabel('Time (t)')
    plt.ylabel('y(t)')
    plt.show()