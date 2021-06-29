from math import ceil

efficiency = 0
for _ in range(3):
    efficiency += int(input())
students = int(input())
time_needed = ceil(students / efficiency)
breaks = time_needed // 3
if time_needed % 3 == 0:
    breaks -= 1
time_needed += breaks
if not students == 0:
    print(f"Time needed: {time_needed}h.")
else:
    print(f'Time needed: 0h.')
