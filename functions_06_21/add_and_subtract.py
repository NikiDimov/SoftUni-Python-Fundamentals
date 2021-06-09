first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_numbers(first, second):
    return first + second


def subtract(first, second, third):
    return sum_numbers(first, second) - third


def add_and_subtract(first, second, third):
    print(subtract(first, second, third))


add_and_subtract(first_num, second_num, third_num)
