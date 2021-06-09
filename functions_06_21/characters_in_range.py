first_char = input()
second_char = input()


def chars_in_range(first, second):
    result = []
    for i in range(ord(first)+1, ord(second)):
        result.append(chr(i))
    return ' '.join(result)


print(chars_in_range(first_char, second_char))
