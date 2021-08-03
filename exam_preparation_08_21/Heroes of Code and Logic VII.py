n = int(input())
heroes = {}
MAX_HP = 100
MAX_MP = 200


def checker(index, name, quantity, maxx):
    if heroes[name][index] + quantity <= maxx:
        amount_recovered = quantity
    else:
        amount_recovered = maxx - heroes[name][index]
    return amount_recovered


for _ in range(n):
    data = input().split()
    hero, HP, MP = data[0], int(data[1]), int(data[2])
    heroes[hero] = [HP, MP]
command = input()
while not command == "End":
    data = command.split(" - ")
    if data[0] == "CastSpell":
        hero_name, MP_needed, spell_name = data[1], int(data[2]), data[3]
        if heroes[hero_name][1] >= MP_needed:
            heroes[hero_name][1] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif data[0] == "TakeDamage":
        hero_name, damage, attacker = data[1], int(data[2]), data[3]
        if damage < heroes[hero_name][0]:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif data[0] == "Recharge":
        hero_name, amount = data[1], int(data[2])
        recharge = checker(1, hero_name, amount, MAX_MP)
        print(f"{hero_name} recharged for {recharge} MP!")
        heroes[hero_name][1] += recharge
    elif data[0] == "Heal":
        hero_name, amount = data[1], int(data[2])
        heal = checker(0, hero_name, amount, MAX_HP)
        print(f"{hero_name} healed for {heal} HP!")
        heroes[hero_name][0] += heal

    command = input()

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in heroes.items():
    print(key)
    print(f" HP: {value[0]}\n MP: {value[1]}")
