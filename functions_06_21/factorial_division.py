first_num = int(input())
second_num = int(input())


def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def division(n1, n2):
    return f"{get_factorial(n1) / get_factorial(n2):.2f}"


print(division(first_num, second_num))
