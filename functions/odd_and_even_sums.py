def function(long_number):
    sum_even = 0
    sum_odd = 0
    long_number = str(long_number)
    for i in range(len(long_number)):
        if int(long_number[i]) % 2 == 0:
            sum_even += int(long_number[i])
        elif int(long_number[i]) % 2 == 1:
            sum_odd += int(long_number[i])
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


num = int(input())
print(function(num))
