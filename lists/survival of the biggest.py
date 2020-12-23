list_of_integer = input().split()
numbers_to_remove = int(input())
new_list = []

for el in list_of_integer:
    new_list.append(int(el))

for i in range(numbers_to_remove):
    new_list.remove(min(new_list))
print(new_list)






















