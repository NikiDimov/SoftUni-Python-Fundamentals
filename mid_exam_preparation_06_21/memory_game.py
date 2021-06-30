sequence = input().split()
command = input()
counter = 0
is_mission_complete = False
while not command == 'end':
    indices = command.split()
    index1, index2 = int(indices[0]), int(indices[1])
    counter += 1
    if index1 == index2 or index1 not in range(0, len(sequence)) or index2 not in range(0, len(sequence)):
        print("Invalid input! Adding additional elements to the board")
        sequence = sequence[:len(sequence) // 2] + 2 * [f"-{counter}a"] + sequence[len(sequence) // 2:]
    else:
        if sequence[index1] == sequence[index2]:
            print(f"Congrats! You have found matching elements - {sequence[index1]}! ")
            element_to_remove = sequence[index1]
            sequence.remove(element_to_remove)
            sequence.remove(element_to_remove)
            if len(sequence) == 0:
                print(f"You have won in {counter} turns!")
                is_mission_complete = True
                break
        else:
            print("Try again!")

    command = input()
if not is_mission_complete:
    print("Sorry you lose :(")
    print(*sequence, sep=' ')
