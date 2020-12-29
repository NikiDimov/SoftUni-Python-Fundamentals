products_in_stock = input().split()
products_in_stock_dict = {}
for index in range(0, len(products_in_stock), 2):
    key = products_in_stock[index]
    value = products_in_stock[index+1]
    products_in_stock_dict[key] = int(value)
search_product = input().split()
for product in search_product:
    if product in products_in_stock_dict.keys():
        print(f"We have {products_in_stock_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


