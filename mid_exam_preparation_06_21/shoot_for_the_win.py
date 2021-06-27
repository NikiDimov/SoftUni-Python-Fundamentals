targets = [int(el) for el in input().split()]
index = input()
shot_targets = 0
while not index == "End":
    index = int(index)
    if index not in range(0, len(targets)) or targets[index] == -1:
        index = input()
        continue
    value = targets[index]
    targets[index] = -1
    shot_targets += 1
    for i in range(len(targets)):
        if targets[i] > value:
            targets[i] -= value
        elif targets[i] <= value and not targets[i] == -1:
            targets[i] += value
    index = input()
print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets))}")

