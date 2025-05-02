diameter = input("Enter the diameter of the sphere: ")
pi = 3.14159265359
r = float(diameter)/2
area = 4 * pi * r**2
volume = (4/3) * pi * r**3
print(f"The surface area of the sphere is {round(area, 3)} \n The volume of the sphere is {round(volume, 3)}")