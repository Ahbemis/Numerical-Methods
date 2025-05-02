# Homework 3.py
# #DESCRIPTION: Numerical Methods Homework 3
# AUTHOR: Andrew Bemis
# DATE: 9/30/2021
# 
# This program contains a series of functions that calculate the range and maximum height of a projectile, the efficiency of a heat engine, temperature conversions, and the summation of a series.

import math

# Problem 1: Projectile Motion Calculator.
# This function calculates the range and maximum height of a projectile based on user-provided initial velocity and launch angle.
def projectile_motion():
    
    v = float(input("Enter the initial velocity of the projectile (m/s): "))
    theta = float(input("Enter the launch angle of the projectile (degrees): "))
    g = 9.81
    theta_rad = math.radians(theta)
    range = (v**2 * math.sin(2 * theta_rad)) / g
    print(f"The range of the projectile is {round(range, 3)} meters")

# Problem 2: Efficiency of a Heat Engine
# This function calculates the efficiency of a heat engine based on user-provided values of the hot reservoir and cold reservoir temperatures.
def heat_engine_efficiency():
    T_hot = float(input("Enter T_H (Kelvin): "))
    T_cold = float(input("Enter T_C (Kelvin): "))
    efficiency = ((T_cold / T_hot) + (-1)) * 100
    print(f"The efficiency of the heat engine is {round(efficiency, 3)}%")

# Problem 3: Temperature Converter
# This function converts temperatures between Fahrenheit, Celsius, Kelvin, and Rankine.
def temperature_conversion():
    while True:
        
        Temp = (input("What's the Temperature? Include the unit of measurement. \n"))
    
        if Temp[-1].lower() == "f":
            conversion = (float(Temp[:-1]) - 32) * 5/9
            conversion_kelvin = (float(Temp[:-1]) - 32) * 5/9 + 273.15
            conversion_Rankine = (float(Temp[:-1]) + 459.67)
            print(f"{round(conversion_Rankine, 3)} R" + "\n" + f"{round(conversion, 3)} C" + "\n" + f"{round(conversion_kelvin, 3)} K")
        elif Temp[-1].lower() == "c":
            conversion = (float(Temp[:-1]) * 9/5) + 32
            conversion_kelvin = float(Temp[:-1]) + 273.15
            conversion_Rankine = float(Temp[:-1]) * 9/5 + 491.67
            print(f"{round(conversion_Rankine, 3)} R" + "\n" + f"{round(conversion, 3)} F" + "\n" + f"{round(conversion_kelvin, 3)} K")
        elif Temp[-1].lower() == "k":
            conversion = (float(Temp[:-1]) - 273.15) * 9/5 + 32
            conversion_celsius = float(Temp[:-1]) - 273.15
            conversion_Rankine = (float(Temp[:-1]) * 9/5)
            print(f"{round(conversion_Rankine, 3)} R" + "\n" + f"{round(conversion, 3)} F" + "\n" + f"{round(conversion_celsius, 3)} C")
        elif Temp[-1].lower() == "r":
            conversion = (int(Temp[:-1]) - 491.67) * 5/9
            conversion_kelvin = float(Temp[:-1]) * 5/9
            conversion_fahrenheit = float(Temp[:-1]) + 459.67
            print(f"{round(conversion_fahrenheit, 3)} F" + "\n" + f"{round(conversion, 3)} C" + "\n" + f"{round(conversion_kelvin, 3)} K")
        else:
            print("Invalid Input. Please include the unit of measurement.") 
            continue
        if input("Convert another temperature? (y/n): ").lower() == 'n':
            break

# Problem 4: Summation of a Series
# This function calculates the summation of the series 1/n^2 for a user-provided number of terms.
def series_summation():
    n = int(input("Enter the number of terms in the series: "))
    total = 0
    for i in range(1, n + 1):
        total += 1 / (i**2)
    compare = total/(3.14159265359**2/6)
    print(f"The sum of the series is {round(total, 4)}, which is approximately {round(compare, 4)} times pi^2/6")
    return total

# Main menu to select different calculators.
while True:
    print("          MAIN MENU          ")
    print("1. Projectile Motion Calculator")
    print("2. Heat Engine Efficiency Calculator")
    print("3. Temperature Converter")
    print("4. Summation of the 1/n^2 Series")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        projectile_motion()
    elif choice == "2":
        heat_engine_efficiency()
    elif choice == "3":
        temperature_conversion()
    elif choice == "4":
        series_summation()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")