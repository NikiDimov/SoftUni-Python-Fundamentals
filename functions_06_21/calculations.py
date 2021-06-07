operator = input()
first_num = int(input())
second_num = int(input())


def calculator(op, first, second):
    if op == "multiply":
        return first * second
    elif op == "divide":
        return first // second
    elif op == "add":
        return first + second
    elif op == "subtract":
        return first - second


print(calculator(operator, first_num, second_num))

