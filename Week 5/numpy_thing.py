import numpy as np # type: ignore

#defining an array

A = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]])
b = np.array([A, A])
print(b)

import matplotlib.pyplot as plt # type: ignore

# Define the slope (m) and intercept (b)
m = 1
b = 0

# Generate x values
x = np.linspace(0, 10, 5)

# Calculate y values
y = m * x + b

# Create the plot
plt.plot(x, y, 'go-', label=f'y={m}x+{b}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y=mx+b')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# set boundaries
plt.xlim(0, 10)
plt.ylim(0, 10)


# print(A)
# print()

# print(A[1][1][1]) # 8
# print()

# print(A[0:1])
# print()

# print(A[1:])
# print()

# print(A+2)
# print()

# print(A*2)
# print()