#AUTHOR: ANDREW BEMIS
#DATE: 2/4/2025
#DESCRIPTION: Numerical Methods Homework 1
#CHECKED BY: ALEXANDER WATTS

# PROBLEM 1: CYLINDER VOLUME CALCULATOR
def cylinder():
    # This function calculates the volume and surface area of a cylinder
    # based on user-provided radius and height.
    radius = input("Enter the radius of the cylinder: ")
    height = input("Enter the height of the cylinder: ")
    pi = 3.14159265359
    r = float(radius)
    h = float(height)
    volume = float(pi) * r**2 * h
    surface_area = 2 * pi * r * h + 2 * pi * r**2
    print(f"The volume of the cylinder is {round(volume, 3)}")
    print(f"The surface area of the cylinder is {round(surface_area, 3)}")

# cylinder()


# PROBLEM 2: BEAM DEFLECTION CALCULATOR
def beam_deflection():
    # This function calculates the deflection of a beam under a load
    # based on user-provided modulus of elasticity, moment of inertia,
    # length of the beam, and applied load.
    E = float(input("Enter the modulus of elasticity: "))
    I = float(input("Enter the moment of inertia: "))
    L = float(input("Enter the length of the beam: "))
    F = float(input("Enter the load applied to the beam: "))
    deflection = (F * L**3) / (48 * E * I)
    print(f"The deflection of the beam is {round(deflection, 3)}")

# beam_deflection()

# PROBLEM 3: SPEED CONVERTER
def speed_converter():
    # This function converts speed from meters per second (m/s) to
    # miles per hour (mph) and kilometers per hour (kph).
    speed = input("Enter the speed in m/s: ")
    speed_mph = float(speed) / 0.44704
    speed_kph = float(speed) * 3.6
    print(f"The speed in mph is {round(speed_mph, 3)}")
    print(f"The speed in kph is {round(speed_kph, 3)}")

# speed_converter()

# PROBLEM 4: QUADRATIC SOLVER
def quadratic_solver():
    # This function solves a quadratic equation of the form ax^2 + bx + c = 0
    # and prints the real or complex solutions based on user-provided coefficients.
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    if b**2 - 4 * a * c < 0:
        print("The solutions are complex.")
    else:
        print(f"The solutions are x = {x1} and x = {x2}")
        print("The solutions are real.")

# quadratic_solver()

# PROBLEM 5: FLUID FLOW ANALYSIS
def fluid_flow():
    # This function analyzes the type of fluid flow (laminar, transitional, or turbulent)
    # based on user-provided density, viscosity, flow rate, and pipe diameter.
    rho = float(input("Enter the density of the fluid: "))
    mu = float(input("Enter the viscosity of the fluid: "))
    Q = float(input("Enter the flow rate of the fluid: "))
    D = float(input("Enter the diameter of the pipe: "))
    A = 3.14159265359 * (D/2)**2
    V = Q / A
    Re = (rho * V * D) / mu
    if Re < 2000:
        print("The flow is laminar.")
    elif Re >= 2000 and Re < 4000:
        print("The flow is transitional.")
    else:
        print("The flow is turbulent.")
        print(f"The Reynolds number is {round(Re, 3)}")

# fluid_flow()

# PROBLEM 6: GEAR RATIO AND EFFICIENCY
def gear_ratio_efficiency():
    # This function calculates the gear ratio and determines the efficiency
    # of a gear system based on user-provided number of teeth on input and output gears.
    input_gear = float(input("Enter the number of teeth on the input gear: "))
    output_gear = float(input("Enter the number of teeth on the output gear: "))
    I = output_gear / input_gear
    print(f"The gear ratio is {round(I, 3)}")
    if I < 3.0:
        print("The gear system is highly efficient.")
    elif  I >= 3.0 and I <= 5.0:
        print("The gear system is moderately efficient.")
    elif I > 5.0:
        print("The gear system is inefficient.")
    else:
        print("Wrong Input")
    
    
# gear_ratio_efficiency()