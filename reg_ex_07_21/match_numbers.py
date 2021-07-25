import re
line = input()
pattern = r'(^|(?<= ))-?\d+(\.\d+)?($|(?= ))'
result = re.finditer(pattern, line)
for match in result:
    print(match.group(), end=' ')
