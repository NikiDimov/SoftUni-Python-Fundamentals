resource = input()
dictionary = {}
while not resource == "stop":
    quantity = int(input())
    if resource in dictionary:
        dictionary[resource] += quantity
    else:
        dictionary[resource] = quantity
    resource = input()

for resource, quantity in dictionary.items():
    print(f"{resource} -> {quantity}")
