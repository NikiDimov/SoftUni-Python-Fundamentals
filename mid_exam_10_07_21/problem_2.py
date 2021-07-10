weapon = input().split("|")
command = input()
while not command == "Done":
    data = command.split()
    if data[0] == "Add":
        particle, index = data[1], int(data[2])
        if index in range(0, len(weapon)):
            weapon.insert(index, particle)
    elif data[0] == "Remove":
        index = int(data[1])
        if index in range(0, len(weapon)):
            weapon.pop(index)
    elif data[0] == "Check":
        if data[1] == "Even":
            print(*weapon[::2], sep=' ')
        elif data[1] == "Odd":
            print(*weapon[1::2], sep=' ')
    command = input()
print(f"You crafted {''.join(weapon)}!")
