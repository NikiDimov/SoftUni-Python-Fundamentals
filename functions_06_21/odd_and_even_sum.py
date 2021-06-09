num = [int(el) for el in list(input())]


def sum_of_odd_digits():
    sum_odd = 0
    for el in num:
        if el % 2 == 1:
            sum_odd += el
    return sum_odd


def sum_of_even_digits():
    sum_even = 0
    for el in num:
        if el % 2 == 0:
            sum_even += el
    return sum_even


print(f"Odd sum = {sum_of_odd_digits()}, Even sum = {sum_of_even_digits()}")
