# first_line = input().split(", ")
# second_line = input().split(", ")
# third_line = []
# new_list = []
# for el in first_line:
#     for el2 in second_line:
#         if not el2.find(el) == -1:
#             third_line.append(el)
# [new_list.append(el) for el in third_line if el not in new_list]
# print(new_list)

list_1 = input().split(", ")
list_2 = input()
new_list = [el for el in list_1 if el in list_2]

print(new_list)
