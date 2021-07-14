products_quantity = {}
products_price = {}
product = input()
while not product == "buy":
    data = product.split()
    name, price, quantity = data[0], float(data[1]), int(data[2])
    products_price[name] = price
    if name not in products_quantity:
        products_quantity[name] = quantity
    else:
        products_quantity[name] += quantity
    product = input()
orders = {}
for k in products_quantity:
    orders[k] = f"{products_quantity[k] * products_price[k]:.2f}"
for k, v in orders.items():
    print(f"{k} -> {v}")

