string_data = input()
repeat_count_n = int(input())


def func(data, n):
    result = ''
    for i in range(n):
        result = result + data
    return result


print(func(string_data, repeat_count_n))
