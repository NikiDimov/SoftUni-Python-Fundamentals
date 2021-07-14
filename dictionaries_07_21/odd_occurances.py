line = [el.lower() for el in input().split()]
dict_line = {}
for el in line:
    value = line.count(el)
    if value % 2 == 1:
        dict_line[el] = value
print(*dict_line, sep=' ')

