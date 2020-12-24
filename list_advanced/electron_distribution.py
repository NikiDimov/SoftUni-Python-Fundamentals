sum_list = int(input())
new_list = []
index = 0
while sum(new_list) <= sum_list:
    index += 1
    new_list.append(2 * (index ** 2))
new_list.pop()
if not sum(new_list) == sum_list:
    new_list.append(sum_list-sum(new_list))
print(new_list)
