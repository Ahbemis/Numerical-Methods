import numpy as np
import matplotlib.pyplot as plt

def fit_cubic_polynomial(epsilons, sigmas):
    """
    Fit a cubic polynomial sigma = a0 + a1*eps + a2*eps^2 + a3*eps^3
    using the normal equations for least squares.
    
    Parameters:
    -----------
    epsilons : array-like
        Strain values (independent variable)
    sigmas : array-like
        Stress values (dependent variable)
    
    Returns:
    --------
    a0, a1, a2, a3 : float
        The fitted polynomial coefficients
    """
    # Convert lists to numpy arrays for convenience
    eps = np.array(epsilons, dtype=float)
    sig = np.array(sigmas, dtype=float)
    
    # Calculate the summations
    N = len(eps)
    S_eps     = np.sum(eps)
    S_eps2    = np.sum(eps**2)
    S_eps3    = np.sum(eps**3)
    S_eps4    = np.sum(eps**4)
    S_eps5    = np.sum(eps**5)
    S_eps6    = np.sum(eps**6)
    
    S_sig         = np.sum(sig)
    S_eps_sig     = np.sum(eps*sig)
    S_eps2_sig    = np.sum((eps**2)*sig)
    S_eps3_sig    = np.sum((eps**3)*sig)
    
    # Build the matrices for the normal equations
    A = np.array([
        [N,       S_eps,   S_eps2,   S_eps3],
        [S_eps,   S_eps2,  S_eps3,   S_eps4],
        [S_eps2,  S_eps3,  S_eps4,   S_eps5],
        [S_eps3,  S_eps4,  S_eps5,   S_eps6]
    ], dtype=float)
    
    b = np.array([
        S_sig,
        S_eps_sig,
        S_eps2_sig,
        S_eps3_sig
    ], dtype=float)
    
    # Solve for [a0, a1, a2, a3]
    coeffs = np.linalg.solve(A, b)
    a0, a1, a2, a3 = coeffs
    
    return a0, a1, a2, a3

def main():
    # Example data (dummy)
    # Replace with your real data arrays:
    eps_data = [0.00, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007]
    sig_data = [0.00, 85.1, 158.3, 223.4, 280.2, 328.7, 369.0, 401.0]
    
    # 1) Fit the cubic polynomial
    a0, a1, a2, a3 = fit_cubic_polynomial(eps_data, sig_data)
    
    print("Fitted coefficients:")
    print(f"a0 = {a0:.6f}")
    print(f"a1 = {a1:.6f}")
    print(f"a2 = {a2:.6f}")
    print(f"a3 = {a3:.6f}")
    
    # 2) Generate a smooth curve for plotting
    eps_fit = np.linspace(min(eps_data), max(eps_data), 200)
    sig_fit = a0 + a1*eps_fit + a2*(eps_fit**2) + a3*(eps_fit**3)
    
    # 3) Plot the original data and the best-fit curve
    plt.figure(figsize=(8,6))
    plt.plot(eps_data, sig_data, 'ro', label='Original Data')
    plt.plot(eps_fit, sig_fit, 'b-', label='Fitted Cubic')
    plt.title('Stress vs. Strain with Cubic Polynomial Fit')
    plt.xlabel('Strain (unitless)')
    plt.ylabel('Stress (MPa)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # 4) Plot residuals
    # Compute fitted values at original data points
    sig_fitted_at_data = a0 + a1*np.array(eps_data) \
                            + a2*(np.array(eps_data)**2) \
                            + a3*(np.array(eps_data)**3)
    residuals = np.array(sig_data) - sig_fitted_at_data
    
    plt.figure(figsize=(8,6))
    plt.axhline(0, color='black', linewidth=1)
    plt.plot(eps_data, residuals, 'ro-')
    plt.title('Residuals: Measured Stress - Fitted Stress')
    plt.xlabel('Strain (unitless)')
    plt.ylabel('Residual (MPa)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()