import re

line = input()
pattern = r'(@|#)(?P<word_one>[a-zA-Z]{3,})\1\1(?P<word_two>[a-zA-Z]{3,})\1'

store = {}
result = re.findall(pattern, line)
if result:
    print(f"{len(result)} word pairs found!")
else:
    print("No word pairs found!")
result = re.finditer(pattern, line)
for match in result:
    if match.group("word_one") == match.group("word_two")[::-1]:
        store[match.group("word_one")] = match.group("word_two")
if store:
    output = [f"{k} <=> {v}" for k, v in store.items()]
    print(f"The mirror words are:")
    print(*output, sep=', ')
else:
    print(f"No mirror words!")
