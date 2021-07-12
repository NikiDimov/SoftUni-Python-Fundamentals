countries = input().split(", ")
capitals = input().split(", ")
my_dict = {countries[i]: capitals[i] for i in range(len(countries))}
for key, value in my_dict.items():
    print(f"{key} -> {value}")
