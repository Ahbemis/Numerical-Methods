Temp = (input("What's the Temperature? Include the unit of measurement. \n"))
print("Here are your converted units: ")
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