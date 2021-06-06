items_with_prices = input().split("|")
budget = float(input())
new_prices = []
sum_old_prices = 0
for el in items_with_prices:
    types, price = el.split("->")
    price = float(price)
    if types == "Clothes":
        if price <= 50 and budget >= price:
            sum_old_prices += price
            new_prices.append(price * 1.4)
            budget -= price
    elif types == "Shoes":
        if price <= 35 and budget >= price:
            sum_old_prices += price
            new_prices.append(price * 1.4)
            budget -= price
    elif types == "Accessories":
        if price <= 20.5 and budget >= price:
            sum_old_prices += price
            new_prices.append(price * 1.4)
            budget -= price
profit = sum(new_prices) - sum_old_prices
sum_of_new_prices = sum(new_prices)
new_prices = [f"{el:.2f}" for el in new_prices]
print(' '.join(new_prices))
print(f"Profit: {profit:.2f}")
if budget + sum_of_new_prices >= 150:
    print("Hello, France!")
else:
    print(f"Time to go.")
    