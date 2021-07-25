import re
line = input()
pattern = r'\b(?P<day>\d{2})(?P<sep>/|.|-)(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
result = re.finditer(pattern, line)
for match in result:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
