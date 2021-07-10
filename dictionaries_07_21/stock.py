stock = input().split()
products = input().split()
stock_dict = {}
keys = stock[::2]
values = stock[1::2]
for i in range(len(keys)):
    stock_dict[keys[i]] = values[i]
for product in products:
    if product in stock_dict:
        print(f"We have {stock_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")