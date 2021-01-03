n = int(input())
plants_dict = {}

for _ in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])
    plants_dict[plant] = {"rarity": rarity, "rating": []}
line = input()
while not line == "Exhibition":
    command, value = line.split(": ")
    try:
        if command == "Rate":
            plant, rating = value.split(" - ")
            rating = int(rating)
            plants_dict[plant]["rating"].append(rating)
        elif command == "Update":
            plant, new_rarity = value.split(" - ")
            new_rarity = int(new_rarity)
            plants_dict[plant]["rarity"] = new_rarity
        elif command == "Reset":
            plant = value
            plants_dict[plant]["rating"].clear()
    except:
        print("error")

    line = input()

for key, value in plants_dict.items():
    if plants_dict[key]["rating"]:
        plants_dict[key]["avr"] = sum(plants_dict[key]["rating"]) / len(plants_dict[key]["rating"])
    else:
        plants_dict[key]["avr"] = 0

sorted_plant_dict = sorted(plants_dict.items(), key=lambda x: (-x[1]["rarity"], -x[1]["avr"]))
print("Plants for the exhibition:")
for key, value in sorted_plant_dict:
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['avr']:.2f}")
