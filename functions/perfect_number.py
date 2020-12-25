# def function(number):
#     sums = 0
#
#     for divisor in range(1, perfect_num // 2 + 1):
#         if perfect_num % divisor == 0:
#             sums += divisor
#
#     if sums == perfect_num:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#
#
# perfect_num = int(input())
# function(perfect_num)

def function(number):
    sums = 0
    text = ''

    for divisor in range(1, perfect_num // 2 + 1):
        if perfect_num % divisor == 0:
            sums += divisor

    if sums == perfect_num:
        text = "We have a perfect number!"

    else:
        text = "It's not so perfect."
    return text


perfect_num = int(input())
print(function(perfect_num))
