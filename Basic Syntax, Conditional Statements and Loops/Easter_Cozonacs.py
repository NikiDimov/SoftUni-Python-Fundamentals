budget = float(input())
price_for_flour = float(input())

price_for_pack_eggs = price_for_flour * 0.75
price_for_250_milk = price_for_flour * 1.25/4

current_cozonacs_count = 0
current_colored_eggs = 0
price_for_one_cozonac = price_for_250_milk + price_for_pack_eggs + price_for_flour

while budget - price_for_one_cozonac >= 0:
    current_cozonacs_count += 1
    current_colored_eggs += 3
    budget -= price_for_one_cozonac
    if current_cozonacs_count % 3 == 0:
        lose_eggs = current_cozonacs_count - 2
        current_colored_eggs -= lose_eggs
print(f"You made {current_cozonacs_count} cozonacs! Now you have {current_colored_eggs} eggs and {budget:.2f}BGN left.")


