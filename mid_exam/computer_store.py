def special_discount(final_price):
    if price == "special":
        final_price = final_price - final_price * 0.1
    return final_price


price = input()
total_price_no_taxes = 0

while not (price == "special" or price == "regular"):
    price = float(price)
    if price < 0:
        print("Invalid price!")
        price = 0
    total_price_no_taxes += price
    price = input()
taxes = total_price_no_taxes * 0.2
total_price_with_taxes = total_price_no_taxes + taxes

if total_price_no_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_no_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {special_discount(total_price_with_taxes):.2f}$")
