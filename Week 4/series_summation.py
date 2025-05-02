

def series_summation():
    n = int(input("Enter the number of terms in the series: "))
    total = 0
    for i in range(1, n + 1):
        total += 1 / (i**2)
    print(f"The sum of the series is {round(total, 3)}")
    return total

total = series_summation()

compare = total/(3.14159265359**2/6)
print(compare)