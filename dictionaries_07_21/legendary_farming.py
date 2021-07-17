key_materials = {'shards': 0, 'motes': 0, 'fragments': 0}
junk_materials = {}


def checker(k):
    if key_materials[k] >= 250:
        if k == 'shards':
            print("Shadowmourne obtained!")
        elif k == 'fragments':
            print("Valanyr obtained!")
        elif k == 'motes':
            print("Dragonwrath obtained!")
        key_materials[k] -= 250
        return True


while True:
    success = False
    line = input().split()
    values = line[::2]
    keys = line[1::2]
    keys = [el.lower() for el in keys]
    for i in range(len(keys)):
        if keys[i] in key_materials:
            key_materials[keys[i]] += int(values[i])
            if checker(keys[i]):
                success = True
                break
        else:
            if keys[i] not in junk_materials:
                junk_materials[keys[i]] = int(values[i])
            else:
                junk_materials[keys[i]] += int(values[i])
    if success:
        break

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
for k, v in key_materials.items():
    print(f"{k}: {v}")
for k, v in junk_materials.items():
    print(f"{k}: {v}")
