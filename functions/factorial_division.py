def function(number_1, number_2):
    factorial_1 = 1
    factorial_2 = 1
    result = 0
    for i in range(1, number_1+1):
        factorial_1 = factorial_1 * i
    for i in range(1, number_2+1):
        factorial_2 *= i
    result = f"{(factorial_1 / factorial_2):.2f}"
    return result


num_1 = int(input())
num_2 = int(input())
print(function(num_1, num_2))
