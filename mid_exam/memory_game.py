sequence = input().split()
indexes = input()
counter = 1
while not indexes == "end":
    first_index, second_index = indexes.split()
    first_index = int(first_index)
    second_index = int(second_index)
    if first_index == second_index or first_index not in range(len(sequence)) or\
            second_index not in range(len(sequence)):
        print("Invalid input! Adding additional elements to the board")
        sequence[len(sequence)//2:len(sequence)//2] = [f"-{counter}a", f"-{counter}a"]
    elif len(sequence) > 0:
        if sequence[first_index] == sequence[second_index]:
            print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
            sequence = [el for el in sequence if not el == sequence[first_index]]
            if len(sequence) == 0:
                print(f"You have won in {counter} turns!")
                break
        else:
            print("Try again!")

    counter += 1
    indexes = input()
if len(sequence) > 0:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")