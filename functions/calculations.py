operator = input()
first_int = int(input())
second_int = int(input())


def calculation(op, fi, se):
    if op == "multiply":
        return fi * se
    elif op == "divide":
        return fi // se
    elif op == "add":
        return fi + se
    elif op == "subtract":
        return fi - se


print(calculation(operator, first_int, second_int))
