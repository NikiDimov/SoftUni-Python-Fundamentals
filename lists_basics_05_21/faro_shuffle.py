single_string = input().split()
cycles = int(input())
for _ in range(cycles):
    left_side = single_string[:len(single_string) // 2]
    right_side = single_string[len(single_string) // 2:]
    result = zip(left_side, right_side)
    single_string = [el for tup in tuple(result) for el in tup]
print(single_string)


