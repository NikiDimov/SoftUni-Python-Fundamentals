def add_and_subtract(number_1, number_2, number_3):
    def sum_numbers():
        return number_1 + number_2

    def subtract():
        return sum_numbers() - number_3

    return subtract()


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
