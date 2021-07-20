line = input().split()
first, second = line[0], line[1]
total = 0


def checker(a, b, t):
    for index in range(len(b)):
        t += ord(b[index]) * ord(a[index])
    for index in range(len(b), len(a)):
        t += ord(a[index])
    return t


if not len(first) == len(second):
    if len(first) > len(second):
        print(checker(first, second, total))
    elif len(first) < len(second):
        print(checker(second, first, total))
else:
    for i in range(len(first)):
        total += ord(first[i]) * ord(second[i])
    print(total)
