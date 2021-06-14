employees_happiness = [int(el) for el in input().split()]
factor = int(input())
result = [el * factor for el in employees_happiness]
average_happiness = sum(result) / len(result)
counter_happy = 0
for el in result:
    if el >= average_happiness:
        counter_happy += 1
if counter_happy >= len(result) / 2:
    print(f"Score: {counter_happy}/{len(result)}. Employees are happy!")
else:
    print(f"Score: {counter_happy}/{len(result)}. Employees are not happy!")
