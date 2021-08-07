n = int(input())
plant_dict = {}
for _ in range(n):
    data = input().split("<->")
    plant, rarity = data[0], int(data[1])
    plant_dict[plant] = {"rarity": rarity, "rating": []}
command = input()
while not command == "Exhibition":
    data = command.split(": ")
    try:
        if data[0] == "Rate":
            plant, rating = data[1].split(" - ")
            rating = int(rating)
            plant_dict[plant]['rating'].append(rating)
        elif data[0] == "Update":
            plant, new_rarity = data[1].split(" - ")
            new_rarity = int(new_rarity)
            plant_dict[plant]['rarity'] = new_rarity
        elif data[0] == "Reset":
            plant = data[1]
            plant_dict[plant]['rating'].clear()
    except KeyError:
        print("error")
    command = input()
new_dict = {}
for k, v in plant_dict.items():
    if v['rating']:
        new_dict[k] = [v['rarity'], sum(v['rating']) / len(v['rating'])]
    else:
        new_dict[k] = [v['rarity'], 0]
new_dict = sorted(new_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))
print("Plants for the exhibition:")
for k, v in new_dict:
    print(f"- {k}; Rarity: {v[0]}; Rating: {v[1]:.2f}")
