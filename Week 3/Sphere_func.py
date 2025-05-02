
# This program calculates the surface area and volume of a sphere given the diameter of the sphere
def sphere(diameter):
    
    pi = 3.14159265359  # Value of pi
    r = (diameter)/2  # Radius of the sphere
    surface_area = [4 * pi * r**2 for r in diameter]  # Surface area of the sphere
    volume = [(4/3) * pi * r**3 for r in diameter]  # Volume of the sphere
    return surface_area, volume  # Return the surface area and volume of the sphere

diameter = input("Enter the diameter of the sphere: ")  # User input for the diameter of the sphere
diameter = (map(float, diameter.split(",")))  # Convert the input to a list of floats
output = sphere(diameter)  # Call the sphere function and assign the return values to surface_area and volume

print(f"The surface area of the sphere is {round(output[0], 3)} \nThe volume of the sphere is {round(output[1], 3)}")  # Print the surface area and volume of the sphere

