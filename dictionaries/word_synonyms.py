n = int(input())
dictionary = {}

for index in range(n):
    key = input()
    value = input()
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)

for key, value in dictionary.items():
    print(f"{key} - {', '.join(dictionary[key])}")