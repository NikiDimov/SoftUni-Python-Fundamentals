line = input()
cities = {}
while not line == "Sail":
    city, population, gold = line.split("||")
    population, gold = int(population), int(gold)
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold
    line = input()
events = input()
while not events == 'End':
    data = events.split("=>")
    if data[0] == "Plunder":
        city, people, gold = data[1], int(data[2]), int(data[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[city][0] -= people
        cities[city][1] -= gold
        if cities[city][0] == 0 or cities[city][1] == 0:
            print(f"{city} has been wiped off the map!")
            del cities[city]
    elif data[0] == 'Prosper':
        city, gold = data[1], int(data[2])
        if not gold < 0:
            cities[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")
    events = input()
if cities:
    cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")