
number_of_terms = int((input("Enter the number of terms in the series: ")))
def sum_series(number_of_terms):
    sum_of = 0
    for k in range(0, number_of_terms + 1):
        sum_of += k
    return sum_of
    

column_2 = 0
for i in range(0, number_of_terms + 1):
    column_2 += i
    column_1 = i+1
    print(f"Interation:{column_1-1}, Sum value:{column_2}")
    


print(f"The sum of the series is {round(sum_series(number_of_terms), 3)}")