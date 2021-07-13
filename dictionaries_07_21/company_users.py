command = input()
companies = {}
while not command == "End":
    data = command.split(" -> ")
    company, user = data[0], data[1]
    if company not in companies:
        companies[company] = [user]
    else:
        if user not in companies[company]:
            companies[company].append(user)
    command = input()
companies = dict(sorted(companies.items(), key=lambda x: x[0]))
for k in companies:
    print(k)
    for el in companies[k]:
        print(f"-- {el}")


