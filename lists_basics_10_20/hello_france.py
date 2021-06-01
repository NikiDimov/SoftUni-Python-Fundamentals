collection_of_items = input().split("|")
budget = float(input())
first_budget = budget
sold_items = []
profit = 0

for article in collection_of_items:
    type_item, price_item = article.split("->")
    price_item = float(price_item)

    if type_item == "Clothes" and price_item > 50.00:
        continue
    elif type_item == "Shoes" and price_item > 35.00:
        continue
    elif type_item == "Accessories" and price_item > 20.50:
        continue

    if price_item <= budget:
        budget -= price_item
        price_item = price_item * 1.4
        sold_items.append(price_item)

for el in sold_items:
    print(f"{el:.2f} ", end="")
print()
profit = sum(sold_items) - (first_budget - budget)
print(f"Profit: {profit:.2f}")
if (sum(sold_items) + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


