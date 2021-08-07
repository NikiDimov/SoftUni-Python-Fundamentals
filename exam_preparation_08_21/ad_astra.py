import re

line = input()
pattern = r'(\||#)(?P<item_name>[a-zA-Z ]+)\1(?P<exp_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>\d{1,4}|10000)\1'
total_calories = 0
result = re.finditer(pattern, line)
for match in result:
    total_calories += int(match.group("calories"))
print(f"You have food to last you for: {total_calories//2000} days!")
result = re.finditer(pattern, line)
for match in result:
    print(f"Item: {match.group('item_name')}, "
          f"Best before: {match.group('exp_date')}, "
          f"Nutrition: {match.group('calories')}")
