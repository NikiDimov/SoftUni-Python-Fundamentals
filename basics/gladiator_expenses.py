lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
count = 0

for games in range(1, lost_fights_count+1):
    if games % 2 == 0:
        expenses += helmet_price
    if games % 3 == 0:
        expenses += sword_price
        if games % 2 == 0:
            count = count + 1
            if not count % 2 == 0:
                expenses += shield_price
            else:
                expenses = expenses + shield_price + armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

