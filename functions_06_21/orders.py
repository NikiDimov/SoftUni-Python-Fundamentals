products = {
    "coffee": 1.5,
    "water": 1,
    "coke": 1.4,
    "snacks": 2,
}

product = input()
quantity = int(input())


def order(prod, quan):
    return f"{products[prod] * quan:.2f}"


print(order(product, quantity))
