product_A = input()
quantity_B = float(input())
coffee = 1.5
water = 1.0
coke = 1.4
snacks = 2.0


def func(product, quantity):
    result = 0
    if product == "water":
        result = quantity * water
    elif product == "coffee":
        result = quantity * coffee
    elif product == "coke":
        result = quantity * coke
    elif product == "snacks":
        result = quantity * snacks
    return f"{result:.2f}"


print(func(product_A, quantity_B))
