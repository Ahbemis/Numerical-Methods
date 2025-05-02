# Homework 4
# Numerical Methods and Analysis
# Author: Andrew Bemis
# Date: 2/22/2025
# Topics: Functions, Loops, Data Analysis, Matrix Operations



import numpy as np
# Problem 1
# Beam Deflection Calculation using a for loop
def beam_deflection(q, L, E, I):
    q = float(input("Enter the load on the beam (q): "))
    L = float(input("Enter the length of the beam (L): "))
    E = float(input("Enter the modulus of elasticity (E): "))
    I = float(input("Enter the moment of inertia (I): "))
    deflection = 0
    x = np.linspace(0, L, 10)
    for xi in x:
        deflection += (q * xi) * (L**3 - 2*L*xi**2 + xi**3) / (24*E*I)
        print(f"The deflection at the 'x' point {round(xi, 3)} is {round(deflection, 3)}")
        print(f"The max deflection is {round(deflection, 3)}")
    return deflection


# Problem 2
# Convergence of a numerical solution using a while loop
# Newton's Cooling Law
def newtons_cooling_law():
    # Get initial temperature of the object from user
    T_o = float(input("Enter the initial temperature of the object (T_o): "))

    # Get temperature of the air from user
    T_inf = float(input("Enter the temperature of the air (T_inf): "))

    # Get conduction constant from user
    k = float(input("Enter the conduction constant (k): "))

    iterations = 0  # Initialize iteration counter
    # T_i = T_o  # Initialize the temperature of the object


    # Loop until the temperature difference is less than 0.1
    while abs(T_o - T_inf) > 0.01:
        # Update the temperature of the object using Newton's cooling law
        T_o = T_o - (k * (T_o - T_inf))

        iterations += 1  # Increment iteration counter

        # Print the current temperature of the object
        print(f"The temperature of the object is {round(T_o, 3)}")

        # Print the number of iterations
        print(f"The number of iterations is {iterations}")

        # Print the current temperature difference
        print(f"The temperature difference is {abs(round(T_inf - T_o, 3))}")

        # Check if the number of iterations has reached 100
        if iterations == 500:
            print("The object is not cooling down.")
            break  # Exit the loop if the object is not cooling down
    return iterations  # Return the final temperature of the object

# Problem 3
# Stress distribution in a plate
def stress_distribution():
    
    W = float(input("Enter the width of the plate: "))
    L = float(input("Enter the length of the plate: "))
    k = float(input("Enter the material constant (k): "))
    # Define grid parameters
    x_range = np.linspace(0, W, 5)  # 5 points from x = 0 to x = 10
    y_range = np.linspace(0, L, 4)   # 4 points from y = 0 to y = 5

    print(x_range)
    print(y_range)

    print(" x  |  y  |  stress (N/m^2)")
    print("---------------------------")

    # Nested loop to iterate over x and y positions
    for x in x_range:
        for y in y_range:
            stress = k * (x**2 + y**2)  #Example temperature distribution
        print(f"{x:4.1f} | {y:4.1f} | {stress:10.2f}") # Print formatted output with 1 decimal place for x and y, and 2 decimal places for temperature 
    return stress

# Problem 4
# Matrix operations in structural analysis
def matrix_operations():
    # Define the matrix A
    K = np.array([[12, -6], [-6, 4]])

    # Define the matrix B
    F = np.array([[10], [4]])

    # Add the matrices A and B
    U = np.linalg.solve(K, F)

    # Print the matrices A, B, C, D, and E
    print(f"Matrix U:\n{U}")
    return U

# Problem 5
# Data analysis of temperature measurements
def temp_data_analysis():
    # Define the temperature data
    temp_data = np.array([23.5, 24.1, 22.8, 25.0, 23.9, 24.5, 22.7, 24.8, 23.6, 25.2])

    # Calculate the mean temperature
    mean_temp = np.mean(temp_data)

    # Calculate the standard deviation of the temperature data
    std_dev_temp = np.std(temp_data)

    # Convert the temperature data from Celsius to Fahrenheit and store it as a numpy array
    temp_data_f = np.array([i * 9/5 + 32 for i in temp_data])
    
    # Find the minimum temperature
    min_temp = np.min(temp_data)
    min_temp_f = np.min(temp_data_f)

    # Find the maximum temperature
    max_temp = np.max(temp_data)
    max_temp_f = np.max(temp_data_f)

    # Print the minimum and maximum temperatures
    print(f"The minimum temperature is {min_temp}")
    print(f"The maximum temperature is {max_temp}")
    print(f"The minimum temperature in Fahrenheit is {min_temp_f}")
    print(f"The maximum temperature in Fahrenheit is {max_temp_f}")

    # Print the mean temperature and standard deviation
    print(f"The mean temperature is {mean_temp}")
    print(f"The standard deviation of the temperature data is {std_dev_temp}")
    print(f"The temperature data in Fahrenheit is {temp_data_f}")
    # Print the minimum and maximum temperatures
    print(f"The minimum temperature is {min_temp}")
    print(f"The maximum temperature is {max_temp}")
    print(f"The minimum temperature in Fahrenheit is {min_temp_f}")
    print(f"The maximum temperature in Fahrenheit is {max_temp_f}")
    return mean_temp, std_dev_temp, temp_data_f

while True:
    print("Select an option:")
    print("1. Beam Deflection Calculation")
    print("2. Convergence of a numerical solution using Newton's Cooling Law")
    print("3. Stress distribution in a plate")
    print("4. Matrix operations in structural analysis")
    print("5. Data analysis of temperature measurements")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        beam_deflection(0, 0, 0, 0)
    elif choice == '2':
        newtons_cooling_law()
    elif choice == '3':
        stress_distribution()
    elif choice == '4':
        matrix_operations()
    elif choice == '5':
        temp_data_analysis()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

