import re
line = input()
pattern = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"

result = [el.group()for el in re.finditer(pattern, line)]
print(*result, sep=",")
