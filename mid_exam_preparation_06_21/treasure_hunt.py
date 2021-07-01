treasure = input().split("|")
command = input()
while not command == "Yohoho!":
    data = command.split()
    if data[0] == "Loot":
        for i in range(1, len(data)):
            if not data[i] in treasure:
                treasure.insert(0, data[i])
    elif data[0] == "Drop":
        index = int(data[1])
        if index in range(0, len(treasure)):
            treasure.append(treasure.pop(index))
    elif data[0] == "Steal":
        index = int(data[1])
        print(', '.join(treasure[-index:]))
        del treasure[-index:]
    command = input()

try:
    average_treasure_gain = f"{len(''.join(treasure)) / len(treasure):.2f}"
    print(f"Average treasure gain: {average_treasure_gain} pirate credits.")
except ZeroDivisionError:
    print("Failed treasure hunt.")
