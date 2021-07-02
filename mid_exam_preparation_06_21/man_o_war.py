pirate_ship = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]
max_health = int(input())
command = input()
while not command == "Retire":
    data = command.split()
    if data[0] == "Fire":
        index, damage = int(data[1]), int(data[2])
        if index in range(0, len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)
    elif data[0] == "Defend":
        start_index, end_index, damage = int(data[1]), int(data[2]), int(data[3])
        if start_index in range(0, len(pirate_ship)) and end_index in range(0, len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)
    elif data[0] == "Repair":
        index, health = int(data[1]), int(data[2])
        if index in range(0, len(pirate_ship)):
            if pirate_ship[index]+health > max_health:
                pirate_ship[index] = max_health
            else:
                pirate_ship[index] += health
    elif data[0] == "Status":
        count = 0
        for el in pirate_ship:
            if el < max_health*0.2:
                count += 1
        print(f"{count} sections need repair.")
    command = input()
print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
