sequence = [int(el) for el in input().split(', ')]
bound = max(sequence)
if bound % 10 == 0:
    cycles = bound // 10
else:
    cycles = bound // 10 + 1

for i in range(1, cycles + 1):
    group = [el for el in sequence if el <= i*10]
    for el in group:
        while el in sequence:
            sequence.remove(el)
    print(f"Group of {i*10}'s: {group}")