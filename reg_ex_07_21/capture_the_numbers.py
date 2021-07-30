import re
line = input()
container = []
pattern = r'\d+'
while line:
    result = re.findall(pattern, line)
    container += result
    line = input()
print(*container, sep=' ')
