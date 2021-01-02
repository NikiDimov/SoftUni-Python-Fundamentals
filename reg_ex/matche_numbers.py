import re
text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
numbers = re.finditer(pattern, text)
numbers = [n.group()for n in numbers]
print(*numbers)
