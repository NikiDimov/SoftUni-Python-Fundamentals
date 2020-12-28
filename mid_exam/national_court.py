
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_people = int(input())
time = 0
total_capacity_per_hour = first_employee + second_employee + third_employee

while total_people > 0:
    time += 1
    total_people -= total_capacity_per_hour
    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")





