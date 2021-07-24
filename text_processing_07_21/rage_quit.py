import re

line = input()
rage_line = ''
pattern = r'(?P<chars>\D+)(?P<nums>\d+)'
result = re.finditer(pattern, line)
for el in result:
    rage_line += el.group('chars').upper()*int(el.group('nums'))

print(f"Unique symbols used: {len(set(rage_line))}")
print(f"{rage_line}")