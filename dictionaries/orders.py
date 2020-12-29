order = input()
dict_order = {}
while not order == "buy":
    name, price, quantity = order.split()
    price = float(price)
    quantity = int(quantity)
    if name in dict_order:
        dict_order[name][1] += quantity
        dict_order[name][0] = price
    else:
        dict_order[name] = [price, quantity]
    order = input()

for name in dict_order:
    total_price = dict_order[name][0]*dict_order[name][1]
    print(f"{name} -> {total_price:.2f}")
    