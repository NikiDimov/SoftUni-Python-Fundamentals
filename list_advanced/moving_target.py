sequence_of_targets = input().split()
sequence_of_targets_ints = [int(el) for el in sequence_of_targets]

command = input()
while not command == "End":
    text, index, power_value_radius = command.split()
    index = int(index)
    power_value_radius = int(power_value_radius)
    if text == "Shoot" and index <= len(sequence_of_targets_ints) - 1 and \
            sequence_of_targets_ints[index] > power_value_radius:
        sequence_of_targets_ints[index] -= power_value_radius
    elif text == "Shoot" and index <= len(sequence_of_targets_ints) - 1 and \
            sequence_of_targets_ints[index] <= power_value_radius:
        sequence_of_targets_ints.remove(sequence_of_targets_ints[index])

    elif text == "Strike" and index - power_value_radius > 0 and \
            index + power_value_radius < len(sequence_of_targets_ints) - 1:
        del sequence_of_targets_ints[index - power_value_radius:index + power_value_radius + 1]
    elif text == "Strike" and (index - power_value_radius < 0 or
                               index + power_value_radius > len(sequence_of_targets_ints) - 1):
        print("Strike missed!")

    elif text == "Add" and index <= len(sequence_of_targets_ints) - 1:
        sequence_of_targets_ints.insert(index, power_value_radius)
    elif text == "Add" and index > len(sequence_of_targets_ints) - 1:
        print("Invalid placement!")

    command = input()
output = "|".join([str(el) for el in sequence_of_targets_ints])

print(output)
