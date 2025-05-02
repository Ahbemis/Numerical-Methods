import numpy as np # type: ignore

# Define grid parameters
x_range = np.linspace(0, 10, 5)  # 5 points from x = 0 to x = 10
y_range = np.linspace(0, 5, 4)   # 4 points from y = 0 to y = 5

print(x_range)
print(y_range)

print(" x  |  y  |  Temperature (°C)")
print("---------------------------")

# Nested loop to iterate over x and y positions
for x in x_range:
    for y in y_range:
        temperature = 100 - (x**2 + y**2)  #Example temperature distribution
    print(f"{x:4.1f} | {y:4.1f} | {temperature:10.2f}") # Print formatted output with 1 decimal place for x and y, and 2 decimal places for temperature 


