from math import ceil

efficiency = 0
for _ in range(3):
    efficiency += int(input())
total_people = int(input())
total_hours = ceil(total_people / efficiency)
breaks = total_hours // 3
if total_hours % 3 == 0 and total_hours != 0:
    breaks -= 1
print(f"Time needed: {total_hours + breaks}h.")
