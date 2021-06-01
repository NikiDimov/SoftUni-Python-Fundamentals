names_of_the_gifts = input().split()
output_result = []
new_command = input().split()
while not new_command == ["No", "Money"]:
    new_names = []
    if new_command[0] == "OutOfStock":
        for el in names_of_the_gifts:
            if el == new_command[1]:
                el = "None"
                new_names.append(el)
            else:
                new_names.append(el)
        names_of_the_gifts = new_names
    elif new_command[0] == "Required":
        for i in range(len(names_of_the_gifts)):
            if i == int(new_command[2]):
                new_names.append(new_command[1])
            else:
                new_names.append(names_of_the_gifts[i])
        names_of_the_gifts = new_names
    elif new_command[0] == "JustInCase":
        names_of_the_gifts[-1] = new_command[1]
        for el in names_of_the_gifts:
            new_names.append(el)
        names_of_the_gifts = new_names

    new_command = input().split()

for el in names_of_the_gifts:
    if not el == "None":
        output_result.append(el)

list_to_string = " ".join(map(str, output_result))

print(list_to_string)
