bakery_list = input().split()
bakery_dict = {}
for index in range(0, len(bakery_list), 2):
    key = bakery_list[index]
    value = int(bakery_list[index + 1])
    bakery_dict[key] = value
print(bakery_dict)
