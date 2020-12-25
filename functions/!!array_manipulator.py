def exchange(nums_list, index):
    if 0 <= index < len(nums_list):
        first_part = nums_list[0:index + 1]
        second_part = nums_list[index + 1:]
        exchanged_list = second_part + first_part
        return exchanged_list
    else:
        print("Invalid index")
        return nums_list


def first_odd_elements(nums_list, count):
    new_list = []
    counter = 0
    if count > len(nums_list):
        print("Invalid count")
        return
    for index in range(len(nums_list)):

        if nums_list[index] % 2 == 1 and counter < count:
            counter += 1
            new_list.append(nums_list[index])
    print(new_list)


def firs_even_elements(nums_list, count):
    new_list = []
    counter = 0
    if count > len(nums_list):
        print("Invalid count")
        return
    for index in range(len(nums_list)):

        if nums_list[index] % 2 == 0 and counter < count:
            counter += 1
            new_list.append(nums_list[index])
    print(new_list)


def last_odd_elements(nums_list, count):
    new_list = []
    counter = 0
    if count > len(nums_list):
        print("Invalid count")
        return
    for index in range(len(nums_list) - 1, - 1, -1):

        if nums_list[index] % 2 == 1 and counter < count:
            counter += 1
            new_list.append(nums_list[index])
    print(new_list)


def last_even_elements(nums_list, count):
    new_list = []
    counter = 0
    if count > len(nums_list):
        print("Invalid count")
        return
    for index in range(len(nums_list) - 1, - 1, -1):

        if nums_list[index] % 2 == 0 and counter < count:
            counter += 1
            new_list.append(nums_list[index])
    print(new_list)


def get_max_odd(nums_list):
    filter_only_odds = []
    for el in nums_list:
        if el % 2 == 1:
            filter_only_odds.append(el)
    if len(filter_only_odds) == 0:
        print("No matches")
        return
    max_odd = max(filter_only_odds)
    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == max_odd:
            print(index)
            break


def get_max_even(nums_list):
    filter_only_even = []
    for el in nums_list:
        if el % 2 == 0:
            filter_only_even.append(el)
    if len(filter_only_even) == 0:
        print("No matches")
        return
    max_even = max(filter_only_even)
    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == max_even:
            print(index)
            break


def get_min_odd(nums_list):
    filter_only_odd = []
    for el in nums_list:
        if el % 2 == 1:
            filter_only_odd.append(el)
    if len(filter_only_odd) == 0:
        print("No matches")
        return
    min_even = min(filter_only_odd)
    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == min_even:
            print(index)
            break


def get_min_even(nums_list):
    filter_only_even = []
    for el in nums_list:
        if el % 2 == 0:
            filter_only_even.append(el)
    if len(filter_only_even) == 0:
        print("No matches")
        return

    min_even = min(filter_only_even)
    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == min_even:
            print(index)
            break


numbers_as_string = input().split()
numbers = list(map(int, numbers_as_string))

command = input()

while not command == "end":
    if command.split()[0] == "exchange":
        i = int(command.split()[1])
        numbers = exchange(numbers, i)
    elif command.split()[0] == "max":
        if command.split()[1] == "odd":
            get_max_odd(numbers)
        elif command.split()[1] == "even":
            get_max_even(numbers)

    elif command.split()[0] == "min":
        if command.split()[1] == "odd":
            get_min_odd(numbers)
        elif command.split()[1] == "even":
            get_min_even(numbers)

    elif command.split()[0] == "first":
        c = int(command.split()[1])
        if command.split()[2] == "odd":
            first_odd_elements(numbers, c)
        elif command.split()[2] == "even":
            firs_even_elements(numbers, c)

    elif command.split()[0] == "last":
        c = int(command.split()[1])
        if command.split()[2] == "odd":
            last_odd_elements(numbers, c)
        elif command.split()[2] == "even":
            last_even_elements(numbers, c)

    command = input()

print(numbers)
