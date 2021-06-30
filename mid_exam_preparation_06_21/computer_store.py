price_of_item = input()
total = 0
is_order_valid = True
while not price_of_item == 'special' and not price_of_item == 'regular':
    price_of_item = float(price_of_item)
    if price_of_item <= 0:
        print('Invalid price!')
        price_of_item = input()
        continue
    total += price_of_item
    price_of_item = input()
if total == 0:
    print('Invalid order!')
    is_order_valid = False
taxes = total * 0.2
total_price = total + taxes
if is_order_valid:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------")
    if price_of_item == 'special':
        print(f"Total price: {total_price - total_price * 0.1:.2f}$")
    else:
        print(f"Total price: {total_price:.2f}$")
