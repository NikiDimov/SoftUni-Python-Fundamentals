import re

line = input().lower()
find_it = input().lower()
pattern = fr'\b{find_it}\b'
result = re.findall(pattern, line)
print(len(result))
