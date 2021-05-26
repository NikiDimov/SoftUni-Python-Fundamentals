text = input()
result = []
for index in range(0, len(text)):
    if 65 <= ord(text[index]) <= 90:
        result.append(index)
print(result)
