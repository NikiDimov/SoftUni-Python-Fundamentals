key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
final_key_materials = {}
materials = input().split()
legendary_item = ''
while True:
    for index in range(0, len(materials), 2):
        material = materials[index + 1].lower()
        quantity = int(materials[index])
        if material in key_materials:
            key_materials[material] += quantity
        else:
            key_materials[material] = quantity
        if material == "shards" and key_materials[material] >= 250:
            legendary_item = "Shadowmourne"
            key_materials[material] -= 250
            print(f"{legendary_item} obtained!")
            break
        elif material == "fragments" and key_materials[material] >= 250:
            legendary_item = "Valanyr"
            key_materials[material] -= 250
            print(f"{legendary_item} obtained!")
            break
        elif material == "motes" and key_materials[material] >= 250:
            legendary_item = "Dragonwrath"
            key_materials[material] -= 250
            print(f"{legendary_item} obtained!")
            break
    if legendary_item:
        break
    materials = input().split()

for material, quantity in key_materials.items():
    if material == "shards" or material == "fragments" or material == "motes":
        final_key_materials[material] = quantity
        final_key_materials = dict(sorted(final_key_materials.items(), key=lambda x: x[0]))
    else:
        junk_materials[material] = quantity
        junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))

final_key_materials = dict(sorted(final_key_materials.items(), key=lambda x: x[1], reverse=True))

for material, quantity in final_key_materials.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")
