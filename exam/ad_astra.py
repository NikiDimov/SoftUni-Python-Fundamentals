import re


pattern = r"(#|\|)(?P<item_name>[A-Za-z\s]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"
food = input()
items = []
total_calories = 0
matches = re.finditer(pattern, food)
for match in matches:
    result = match.groupdict()
    total_calories += int(result["calories"])
    items.append(result)
days = total_calories//2000
print(f"You have food to last you for: {days} days!")
for food in items:
    print(f"Item: {food['item_name']}, Best before: {food['exp_date']}, Nutrition: {food['calories']}")


