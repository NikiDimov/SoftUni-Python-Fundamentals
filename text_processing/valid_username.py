user_names = input().split(", ")
container = []
for user_name in user_names:
    if 3 <= len(user_name) <= 16:
        container.append(user_name)
        for el in user_name:
            if el.isalpha() or el.isdigit() or el == "-" or el == "_":
                continue
            container.remove(user_name)
            break

for el in container:
    print(el)
