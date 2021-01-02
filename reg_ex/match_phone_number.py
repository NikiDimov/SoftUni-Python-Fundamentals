import re

text = input()
pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
phones = re.finditer(pattern, text)
phones = [p.group()for p in phones]
print(', '.join(phones))


