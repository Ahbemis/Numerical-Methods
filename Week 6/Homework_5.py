import numpy as np
import matplotlib.pyplot as plt
import time

# Function to calculate the moment of inertia
def moment_of_inertia():
    b = float(input("Enter the base length: "))  # Get base length from user
    h = float(input("Enter the height: "))  # Get height from user

    I = 1/12 * b * h**3  # Calculate moment of inertia
    print(f"The moment of inertia is: {I}")  # Print the result
    return I  # Return the result

# Function to solve axial truss loads using linear algebra
def axial_truss_loads_linsolve():
    a = np.array([[3, 2, -1], [-2, 5, 3], [4, -3, 2]])  # Coefficient matrix
    b = np.array([1000, 500, 200])  # Constant terms

    x = np.linalg.solve(a, b)  # Solve the linear system
    print(f"F1 = {x[0]}, F2 = {x[1]}, F3 = {x[2]}")  # Print the forces
    return x  # Return the forces

# Function to visualize projectile motion
def projectile_motion_visualize():
    v0 = float(input("Enter the initial velocity: "))  # Get initial velocity from user
    theta = np.degrees(float(input("Enter the angle of projection: ")))  # Get angle of projection from user
    g = 9.81  # Acceleration due to gravity

    t = np.linspace(0, 2*v0*np.sin(theta)/g, 100)  # Time array
    x = abs(v0 * np.cos(theta) * t)  # X-coordinates
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2  # Y-coordinates
    print('please close the plot to continue')  # Prompt user to close the plot
    plt.figure(figsize=(6, 5))  # Create a figure
    plt.plot(x, y, label='Projectile Motion', color='b', linestyle='--')  # Plot the projectile motion
    plt.xlabel('x')  # Label for x-axis
    plt.ylabel('y')  # Label for y-axis
    plt.title('Projectile Motion')  # Title of the plot
    plt.legend()  # Show legend
    plt.grid('on')  # Show grid
    plt.show()  # Display the plot

# Function to calculate and visualize temperature distribution on a fin
def heat_transfer_fin():
    T_0 = 150  # Initial temperature
    T_inf = 25  # Ambient temperature
    L = 0.1  # Length of the fin
    m = 5  # Constant
    x = np.linspace(0, L, 10)  # X-coordinates
    T = T_inf + (T_0 - T_inf) * np.exp(-m * x)  # Temperature distribution
    print(f"The temperature at the linearly spaced points on the fin is:\n {T}")  # Print the temperature distribution
    print('please close the plot to continue')  # Prompt user to close the plot
    plt.figure(figsize=(6, 5))  # Create a figure
    plt.plot(x, T, label='Temperature Distribution', color='b', linestyle='--')  # Plot the temperature distribution
    plt.xlabel('x')  # Label for x-axis
    plt.ylabel('T')  # Label for y-axis
    plt.title('Temperature Distribution on the Fin')  # Title of the plot
    plt.legend()  # Show legend
    plt.grid('on')  # Show grid
    plt.show()  # Display the plot

# Function to calculate stress in a rotating disk
def stress_rotating_disk():
    rho = 7850  # Density of the material
    r = 0.1  # Radius of the disk
    omega = 1000  # Angular velocity
    v = 0.3  # Poisson's ratio
    R = 0.15  # Outer radius of the disk
    r = np.linspace(0, 0.2, 10)  # Radial positions
    sigma = (rho * omega**2)/8 * (3 + v - (1 + v) * r**2 / R**2) * R**2  # Stress distribution
    print(f"The stress at the linearly spaced points on the disk is:\n {sigma}")  # Print the stress distribution
    return sigma  # Return the stress distribution

# Main function to display menu and call appropriate functions
def main():

    while True:
        delay = np.random.uniform(1, 5)  # Random delay
        print('\nLoading, please wait...')  # Loading message
        time.sleep(delay)  # Wait for the delay
        print("\nProblem 1. Moment of Inertia")  # Menu option 1
        print("Problem 2. Axial Truss Loads using linsolve")  # Menu option 2
        print("Problem 3. Projectile Motion Visualization")  # Menu option 3
        print("Problem 4. Heat Transfer Fin")  # Menu option 4
        print("Problem 5. Stress in Rotating Disk")  # Menu option 5
        print("6. Exit")  # Menu option 6
        choice = int(input("Choose the problem you would like to see by inputting the number: \n"))  # Get user choice

        if choice == 1:
            moment_of_inertia()  # Call moment_of_inertia function
        elif choice == 2:
            axial_truss_loads_linsolve()  # Call axial_truss_loads_linsolve function
        elif choice == 3:
            projectile_motion_visualize()  # Call projectile_motion_visualize function
        elif choice == 4:
            heat_transfer_fin()  # Call heat_transfer_fin function
        elif choice == 5:
            stress_rotating_disk()  # Call stress_rotating_disk function
        elif choice == 6:
            break  # Exit the loop
        else:
            print("Invalid choice. Please enter a valid choice.")  # Invalid choice message

# Call the main function to start the program
main()
