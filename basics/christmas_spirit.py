quantity = int(input())
days = int(input())
christmas_spirit_count = 0
budget = 0

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        budget += 2 * quantity
        christmas_spirit_count = christmas_spirit_count + 5
    if current_day % 3 == 0:
        budget += 8 * quantity
        christmas_spirit_count = christmas_spirit_count + 13
    if current_day % 5 == 0:
        budget += 15 * quantity
        christmas_spirit_count = christmas_spirit_count + 17
    if current_day % 3 == 0 and current_day % 5 == 0:
        christmas_spirit_count += 30
    if current_day % 10 == 0:
        christmas_spirit_count -= 20
        budget += 23
    if current_day == days and current_day % 10 == 0:
        christmas_spirit_count -= 30

print("Total cost:", budget)
print("Total spirit:", christmas_spirit_count)
