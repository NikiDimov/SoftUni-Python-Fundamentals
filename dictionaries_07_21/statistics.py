products = {}
command = input()
while not command == "statistics":
    key, value = command.split(": ")
    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)
    command = input()
print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
