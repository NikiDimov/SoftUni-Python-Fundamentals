words = input().split()
words = [el.lower() for el in words]
dictionary = {}
final_list = []
value = 1
for index in range(len(words)):
    key = words[index]
    if key in dictionary:
        dictionary[key] += 1
        continue
    dictionary[key] = value
for key, value in dictionary.items():
    if dictionary[key] % 2 == 0:
        continue
    final_list.append(key)
print(' '.join(final_list))