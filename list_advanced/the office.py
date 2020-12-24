employees_happiness = [int(el) for el in input().split()]
factor = int(input())
factored_happiness = list(map(lambda x: x * factor, employees_happiness))
filtered_happiness = list(filter(lambda x: x >= sum(factored_happiness) / len(factored_happiness), factored_happiness))

if len(filtered_happiness) >= len(factored_happiness)/2:
    print(f"Score: {len(filtered_happiness)}/{len(factored_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happiness)}/{len(factored_happiness)}. Employees are not happy!")

