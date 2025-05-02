import numpy as np


def one_point_iteration(func, x0, tol=1e-6, max_iter=100):
    """
    One-point iteration method for finding a root of the equation f(x) = 0.

    Parameters:
        func (callable): The function for which the root is to be found.
        x0 (float): Initial guess for the root.
        tol (float): Tolerance for convergence. Default is 1e-6.
        max_iter (int): Maximum number of iterations. Default is 100.

    Returns:
        float: The approximate root of the function.
        int: The number of iterations performed.
    """
    x = x0
    for i in range(max_iter):
        x_next = func(x) + x
        if abs(x_next - x) < tol:
            return x_next, i + 1
        x = x_next
    raise ValueError("One-point iteration did not converge within the maximum number of iterations.")

# Example usage:
if __name__ == "__main__":
    # Define the function g(x) = x - f(x)/f'(x) or any rearranged form of f(x) = 0
    def g(x):
        return np.exp(-x/4)*(2-x)-1  # Example of a function that converges
    initial_guess = -1
    try:
        root, iterations = one_point_iteration(g, initial_guess)
        print(f"Root: {root}, Iterations: {iterations}")
    except ValueError as e:
        print(e)