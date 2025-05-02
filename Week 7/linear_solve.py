import matplotlib.pyplot as plt

x = [10, 15, 20, 25, 30, 35]
y = [2.2, 4.2, 4.6, 6.6, 7.0, 9.2]

# Calculate the mean of x and y
x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

# Calculate the slope and intercept using the least squares method
numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
denominator = sum((xi - x_mean) ** 2 for xi in x)
slope = numerator / denominator
intercept = y_mean - slope * x_mean

# Generate x values for the fitted line
x_fit = [min(x) + i * (max(x) - min(x)) / 99 for i in range(100)]

# Calculate the corresponding y values using the linear model
y_fit = [slope * xi + intercept for xi in x_fit]

# Plot the data points and the fitted line
plt.plot(x_fit, y_fit, label='Fitted line', color='red')
plt.plot(x, y, 'o', label='Data points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data points')
plt.legend()
plt.grid()
plt.show()
