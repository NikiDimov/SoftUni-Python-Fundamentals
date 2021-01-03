number_of_heroes = int(input())
hero_hit_points = {}
hero_mana_points = {}
for _ in range(number_of_heroes):
    hero = input().split()
    hero_name, HP, MP = hero[0], hero[1], hero[2]
    HP = int(HP)
    MP = int(MP)
    hero_hit_points[hero_name] = HP
    hero_mana_points[hero_name] = MP
line = input()
while not line == "End":
    command = line.split(" - ")
    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_points = int(command[2])
        spell_name = command[3]
        if hero_mana_points[hero_name] >= mana_points:
            hero_mana_points[hero_name] -= mana_points
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_mana_points[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        if hero_hit_points[hero_name] > damage:
            hero_hit_points[hero_name] -= damage
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_hit_points[hero_name]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del hero_hit_points[hero_name]
            del hero_mana_points[hero_name]
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        hero_mana_points[hero_name] += amount
        if hero_mana_points[hero_name] >= 200:
            amount_recovered = 200 - (hero_mana_points[hero_name] - amount)
            print(f"{hero_name} recharged for {amount_recovered} MP!")
            hero_mana_points[hero_name] = 200
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        hero_hit_points[hero_name] += amount
        if hero_hit_points[hero_name] >= 100:
            amount_recovered = 100 - (hero_hit_points[hero_name] - amount)
            print(f"{hero_name} healed for {amount_recovered} HP!")
            hero_hit_points[hero_name] = 100
        else:
            print(f"{hero_name} healed for {amount} HP!")

    line = input()

sorted_hero_hit_points = dict(sorted(hero_hit_points.items(), key=lambda x: (-x[1], x[0])))

for player, hp in sorted_hero_hit_points.items():
    print(player)
    print(f"  HP: {hp}")
    print(f"  MP: {hero_mana_points[player]}")

