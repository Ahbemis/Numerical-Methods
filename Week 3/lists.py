# colors = ["red", "blue", "green", "yellow", "black"]
# print(type(colors))
# print(colors[0:5])  # red
# # print(colors[1])  # blue
# # print(colors[2])  # green
# # print(colors[3])  # yellow
# # print(colors[4])  # black

input_value = [70.85,780,3600]
def numbers(input_value):
    numbers = list(map(float, input_value))
    sum_linear = numbers[0] + numbers[1] + numbers[2]
    sum_squared = numbers[0]**2 + numbers[1]**2 + numbers[2]**2
    sum_cubed = numbers[0]**3 + numbers[1]**3 + numbers[2]**3
    output = [sum_linear, sum_squared, sum_cubed]
    return output

print(numbers(input_value))