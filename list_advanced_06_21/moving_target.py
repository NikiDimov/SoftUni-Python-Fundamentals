targets = [int(el) for el in input().split()]
command = input()
while not command == "End":
    text = command.split()
    if text[0] == "Shoot":
        index, power = int(text[1]), int(text[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                del targets[index]
    if text[0] == "Add":
        index, value = int(text[1]), int(text[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")
    if text[0] == "Strike":
        index, radius = int(text[1]), int(text[2])
        if index - radius < 0 or index + radius >= len(targets):
            print("Strike missed!")
        else:
            del targets[index - radius:index + radius+1]
    command = input()
print('|'.join(map(str, targets)))
