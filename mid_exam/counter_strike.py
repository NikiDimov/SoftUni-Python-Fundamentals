initial_energy = int(input())
counter = 0
while initial_energy >= 0:
    command = input()
    if command == "End of battle":
        break
    else:
        distance = int(command)
        if distance > initial_energy:
            print(f"Not enough energy! Game ends with {counter} won battles and {initial_energy} energy")
        initial_energy -= distance
        counter += 1
        if counter % 3 == 0:
            initial_energy += counter
if initial_energy >= 0:
    print(f"Won battles: {counter}. Energy left: {initial_energy}")


