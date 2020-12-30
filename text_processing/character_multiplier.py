def smallest_string(string1, string2):
    if len(string1) > len(string2):
        min_string = string2
    else:
        min_string = string1
    return min_string


def left_over(string1, string2):
    if len(string1) > len(string2):
        last_parts = string1[len(string2):]
    else:
        last_parts = string2[len(string1):]
    return last_parts


first, second = input().split()
total = 0

for index in range(len(smallest_string(first, second))):
    total += ord(second[index]) * ord(first[index])
if not len(first) == len(second):
    for el in left_over(first, second):
        total += ord(el)
print(total)
