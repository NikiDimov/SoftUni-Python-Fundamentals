text = input()
dictionary = {}

for char in text:
    if not char == " ":
        dictionary[char] = text.count(char)
for key, value in dictionary.items():
    print(f"{key} -> {value}")
