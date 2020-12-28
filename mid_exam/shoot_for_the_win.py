sequence = input().split()
sequence = [int(el) for el in sequence]
index = input()
current_target = 0

counter = 0
while not index == "End":
    index = int(index)
    if index >= len(sequence):
        current_target = 0
    else:
        for i in range(len(sequence)):
            if i == index:
                current_target = sequence[i]
                sequence[i] = -1
                counter += 1
                break

    for i in range(len(sequence)):
        if sequence[i] == -1:
            continue
        elif sequence[i] > current_target:
            sequence[i] -= current_target
        elif sequence[i] <= current_target:
            sequence[i] += current_target

    index = input()

print(f"Shot targets: {counter} -> {' '.join(map(str, sequence))}")
