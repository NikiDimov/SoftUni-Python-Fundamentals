number = int(input())

# for num in range(1, number+1):
#     sum_of_digits = 0
#     digits = num
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits/10)
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")

for num in range(1, number + 1):
    result = 0
    num_as_str = str(num)
    for char in num_as_str:
        result += int(char)
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
