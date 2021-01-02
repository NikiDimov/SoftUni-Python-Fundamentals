import re

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\_.-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+"
result = re.finditer(pattern, text)
for el in result:
    print(el.group())


