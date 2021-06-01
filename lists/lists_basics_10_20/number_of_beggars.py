list_of_numbers = input().split(", ")
beggars = int(input())
list_of_ints = []
output_list = []
add_index = 0

for el in list_of_numbers:
    list_of_ints.append(int(el))

if beggars <= len(list_of_numbers):
    for j in range(0, beggars):
        sum_ints = 0
        for i in range(0, len(list_of_ints), beggars):
            sum_ints += list_of_ints[i]
        output_list.append(sum_ints)
        list_of_ints.pop(0)
    print(output_list)
else:
    for el in list_of_ints:
        add_index = beggars - len(list_of_ints)
        output_list.append(el)
    for i in range(0, add_index):
        output_list.append(0)
    print(output_list)



