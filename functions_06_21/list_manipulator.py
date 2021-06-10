lists = [int(el) for el in input().split()]
command = input()


def exchange(index):
    return lists[index + 1:] + lists[:index + 1]


def checker(r):
    new_list = []
    for i in range(len(lists)):
        if lists[i] == r:
            new_list.append(i)
    return new_list[-1]


def max_even():
    try:
        result = max([el for el in lists if el % 2 == 0])
        return checker(result)
    except:
        return "No matches"


def max_odd():
    try:
        result = max([el for el in lists if el % 2 == 1])
        return checker(result)
    except:
        return "No matches"


def min_even():
    try:
        result = min([el for el in lists if el % 2 == 0])
        return checker(result)
    except:
        return "No matches"


def min_odd():
    try:
        result = min([el for el in lists if el % 2 == 1])
        return checker(result)
    except:
        return "No matches"


def find_evens():
    result = []
    for el in lists:
        if el % 2 == 0:
            result.append(el)
    return result


def find_odds():
    result = []
    for el in lists:
        if el % 2 == 1:
            result.append(el)
    return result


def first_even_counter(count):
    if count > len(lists):
        return "Invalid count"

    result = find_evens()
    result = result[:count]
    return result


def first_odd_counter(count):
    if count > len(lists):
        return "Invalid count"
    result = find_odds()
    result = result[:count]
    return result


def last_even_counter(count):
    if count > len(lists):
        return "Invalid count"
    result = find_evens()
    return result[-count:]


def last_odd_counter(count):
    if count > len(lists):
        return "Invalid count"
    result = find_odds()
    return result[-count:]


while not command == "end":
    list_commands = command.split()
    if list_commands[0] == "exchange":
        index = int(list_commands[1])
        if index in range(0, len(lists)):
            lists = exchange(index)
        else:
            print("Invalid index")
    elif list_commands[0] == "max":
        if list_commands[1] == "even":
            print(max_even())
        elif list_commands[1] == "odd":
            print(max_odd())
    elif list_commands[0] == "min":
        if list_commands[1] == "even":
            print(min_even())
        elif list_commands[1] == "odd":
            print(min_odd())
    elif list_commands[0] == "first":
        if list_commands[2] == "even":
            print(first_even_counter(int(list_commands[1])))
        elif list_commands[2] == "odd":
            print(first_odd_counter(int(list_commands[1])))
    elif list_commands[0] == "last":
        if list_commands[2] == "even":
            print(last_even_counter(int(list_commands[1])))
        elif list_commands[2] == "odd":
            print(last_odd_counter(int(list_commands[1])))

    command = input()
print(lists)
