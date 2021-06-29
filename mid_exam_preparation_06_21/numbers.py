sequence = sorted([int(el) for el in input().split()])
average_value = sum(sequence) / len(sequence)
result = [el for el in sequence[::-1] if el > average_value]
if result:
    print(' '.join(map(str, result[:5])))
else:
    print("No")
