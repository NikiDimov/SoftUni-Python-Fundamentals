budget = float(input())
kg_flour_price = float(input())

price_for_pack_of_eggs = kg_flour_price * 0.75
price_for_l_milk = kg_flour_price * 1.25
needed_milk_price = price_for_l_milk * 0.25
total_price_for_one_cozonac = price_for_pack_of_eggs + kg_flour_price + needed_milk_price

total_cozonacs = int(budget // total_price_for_one_cozonac)
total_eggs = 0

for current_cozonac in range(1, total_cozonacs + 1):
    total_eggs += 3
    budget -= total_price_for_one_cozonac
    if current_cozonac % 3 == 0:
        total_eggs = total_eggs - (current_cozonac - 2)
print(f"You made {total_cozonacs} cozonacs! Now you have {total_eggs} eggs and {budget:.2f}BGN left.")

