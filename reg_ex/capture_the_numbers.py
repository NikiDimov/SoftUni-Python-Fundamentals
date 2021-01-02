import re
text = input()
pattern = r"\d+"
numbers = []
while text:
    match = re.findall(pattern, text)
    if match:
        numbers.extend(match)

    text = input()
print(*numbers, sep=" ")
