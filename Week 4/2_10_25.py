# This is the Loops lecture
from Homework1 import cylinder, beam_deflection, speed_converter, quadratic_solver
import time
while True:
    time.sleep(5)
    print("          MAIN MENU          ")
    print("1. Cylinder Volume Calculator")
    print("2. Beam Deflection Calculator")
    print("3. Speed Converter")
    print("4. Quadratic Solver")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        cylinder()
    elif choice == "2":
        beam_deflection()
    elif choice == "3":
        speed_converter()
    elif choice == "4":
        quadratic_solver()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")