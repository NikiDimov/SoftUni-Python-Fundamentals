first_string = list(input())
second_string = list(input())

for i in range(0, len(first_string)):
    if first_string[i] == second_string[i]:
        continue
    first_string[i] = second_string[i]
    print(''.join(first_string))




