initial_health = 100
current_health = initial_health
initial_bitcoins = 0
dungeon_rooms = input().split("|")
counter = 0
for room in dungeon_rooms:
    counter += 1
    command, number = room.split()
    number = int(number)
    if command == "potion":
        if current_health < 100:
            add = 100 - current_health
            if add <= number:
                current_health += add
                print(f"You healed for {add} hp.")
            else:
                current_health += number
                print(f"You healed for {number} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        current_health -= number
        if not current_health <= 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter}")
            break

if counter == len(dungeon_rooms):
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {current_health}")

