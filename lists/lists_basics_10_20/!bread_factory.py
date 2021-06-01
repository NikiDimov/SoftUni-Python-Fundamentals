working_day_events = input().split("|")
initial_energy = 100
initial_coins = 100
current_energy = initial_energy
current_coins = initial_coins
counter = 0

for el in working_day_events:
    event_ingredient, number = el.split("-")
    number = int(number)
    counter += 1
    if event_ingredient == "rest":
        current_energy += number
        if current_energy >= initial_energy:
            print(f"You gained {abs(current_energy - initial_energy - number)} energy.")
            print(f"Current energy: {initial_energy}.")
            current_energy = initial_energy
        else:
            print(f"You gained {number} energy.")
            print(f"Current energy: {current_energy}.")
    elif event_ingredient == "order":

        current_energy -= 30
        if current_energy >= 0:
            print(f"You earned {number} coins.")
            current_coins += number
        else:
            print("You had to rest!")
            current_energy += 50
    else:
        current_coins -= number
        if not current_coins <= 0:
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            break
if counter == len(working_day_events):
    print(f"Day completed!\nCoins: {current_coins}\nEnergy: {current_energy}")

