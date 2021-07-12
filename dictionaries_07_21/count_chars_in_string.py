line = input()
my_dict = {}
for el in line:
    if not el == ' ':
        value = line.count(el)
        my_dict[el] = value
for key, value in my_dict.items():
    print(f"{key} -> {value}")

