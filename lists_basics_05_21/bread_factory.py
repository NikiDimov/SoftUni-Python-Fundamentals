current_energy = 100
current_coins = 100
finish_the_order = True
events = input().split("|")
for el in events:
    command, number = el.split("-")
    number = int(number)
    if command == "rest":
        if current_energy + number > 100:
            print(f"You gained {100 - current_energy} energy.")
            current_energy = 100
        else:
            print(f"You gained {number} energy.")
            current_energy += number
        print(f"Current energy: {current_energy}.")
    elif command == "order":
        if current_energy-30 >= 0:
            current_coins += number
            current_energy -= 30
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print(f"You had to rest!")
    else:
        if not current_coins-number <= 0:
            current_coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            finish_the_order = False
            break
if finish_the_order:
    print(f"Day completed!\nCoins: {current_coins}\nEnergy: {current_energy}")
