bakery = input().split()
values = bakery[1::2]
keys = bakery[::2]
bakery_dict = {}
for i in range(len(keys)):
    bakery_dict[keys[i]]=int(values[i])
print(bakery_dict)

