company = input()
dictionary = {}
while not company == "End":
    company_name, employee_id = company.split(" -> ")
    if company_name not in dictionary:
        dictionary[company_name] = []
    if employee_id not in dictionary[company_name]:
        dictionary[company_name].append(employee_id)

    company = input()
dictionary = sorted(dictionary.items(), key=lambda x: x[0])

for name, employ_id in dictionary:
    print(f"{name}")
    for el in employ_id:
        print(f"-- {el}")
