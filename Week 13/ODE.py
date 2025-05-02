# ODE.py
# Solving an ODE using Euler's Method

def euler_method(f, y0, t0, t_end, h):
    """
    Solves an ODE using Euler's method.

    Parameters:
        f: Function representing dy/dt = f(t, y)
        y0: Initial value of y
        t0: Initial time
        t_end: End time
        h: Step size

    Returns:
        t_values: List of time values
        y_values: List of y values
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        y = y + h * f(t, y)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Example usage
if __name__ == "__main__":
    # Define the ODE dy/dt = -2y
    def f(t, y):
        return -2 * y

    # Initial conditions
    y0 = 1
    t0 = 0
    t_end = 5
    h = 0.1

    # Solve the ODE
    t_values, y_values = euler_method(f, y0, t0, t_end, h)

    # Print results
    for t, y in zip(t_values, y_values):
        print(f"t = {t:.2f}, y = {y:.4f}")

    # Plotting the results
    import matplotlib.pyplot as plt
    plt.plot(t_values, y_values, label='Euler Method')
    plt.title("Euler's Method for ODE")
    plt.legend()
    plt.grid()
    plt.xlabel('Time (t)')
    plt.ylabel('y(t)')
    plt.show()
    