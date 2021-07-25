import re
line = input()
pattern = r'(^|(?<= ))\+359(\s|-)2\2\d{3}\2\d{4}\b'
output = []
result = re.finditer(pattern, line)
for r in result:
    output.append(r.group())
print(*output, sep=', ')