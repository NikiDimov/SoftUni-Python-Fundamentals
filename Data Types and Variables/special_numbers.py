num = int(input())
for i in range(1, num+1):
    sum_of_digits = 0
    for el in str(i):
        sum_of_digits += int(el)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
