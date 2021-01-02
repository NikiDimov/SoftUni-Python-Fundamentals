import re

text = input()
searched = input()
pattern = f"\\b{searched}\\b"
result = re.findall(pattern, text, re.IGNORECASE)
print(len(result))

