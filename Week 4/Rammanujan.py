import math

def ramanujan_pi(n_terms):
    sum_series = 0
    for k in range(n_terms):
        numerator = math.factorial(4*k) * (1103 + 26390*k)
        denominator = (math.factorial(k)**4) * (396**(4*k))
        sum_series += numerator / denominator
    constant_factor = (2 * math.sqrt(2)) / 9801
    pi_inverse = constant_factor * sum_series
    return 1 / pi_inverse

# Example usage
n_terms = int(input("how many interations would you like to run?: "))
pi_approx = ramanujan_pi(n_terms)
error = ((pi_approx - math.pi) / math.pi) * 100
print(f"{math.pi}")
print(f"Approximation of Pi using {n_terms} terms: {pi_approx}, which is approximately {error}% error")