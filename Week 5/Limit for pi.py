import numpy as np
import math
import matplotlib.pyplot as plt
sum = 0
def ramanujan_pi(n_terms):
    sum_series = 0
    for k in range(n_terms):
        numerator = math.factorial(4*k) * (1103 + 26390*k)
        denominator = (math.factorial(k)**4) * (396**(4*k))
        sum_series += numerator / denominator
    constant_factor = (2 * math.sqrt(2)) / 9801
    pi_inverse = constant_factor * sum_series
    return 1 / pi_inverse

n_terms = np.array([1, 2, 3, 4, 5, 6])
sum_pi_values = []

for term in n_terms:
    sum += ramanujan_pi(term)
    sum_pi_values.append(ramanujan_pi(term))

plt.plot(n_terms, sum_pi_values, 'go-', label='Pi values')
plt.ylim(0, 4)
plt.legend()
plt.xlabel('Number of terms')
plt.ylabel('Pi values')
plt.title('Plot of Pi values')
plt.show()

print(f"Sum of Pi values: {sum_pi_values}")
