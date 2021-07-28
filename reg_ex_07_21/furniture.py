import re

pattern = r'^>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+$)'
total_money = 0
my_furniture = []
products = input()
while not products == 'Purchase':
    result = re.finditer(pattern, products)
    for product in result:
        my_furniture.append(product.group('furniture'))
        total_money += float(product.group('price')) * int(product.group('quantity'))

    products = input()
print('Bought furniture:')
for furniture in my_furniture:
    print(furniture)
print(f'Total money spend: {total_money:.2f}')
