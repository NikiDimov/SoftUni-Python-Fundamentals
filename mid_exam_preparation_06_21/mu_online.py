initial_health = 100
initial_bitcoins = 0
rooms = input().split('|')
is_alive = True
for room in rooms:
    command, number = room.split()
    number = int(number)
    if command == "potion":
        if initial_health + number > 100:
            print(f"You healed for {100 - initial_health} hp.")
            initial_health = 100
        else:
            initial_health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if initial_health > number:
            initial_health -= number
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room)+1}")
            is_alive = False
            break
if is_alive:
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}")
