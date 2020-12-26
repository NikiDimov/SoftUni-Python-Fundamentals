class Zoo:
    __animals = 0

    def __init__(self, title):
        self.name = title
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result
        # animals_to_display = []
        # if species == "mammal":
        #     animals_to_display = self.mammals
        # elif species == "bird":
        #     animals_to_display = self.birds
        # elif species == "fish":
        #     animals_to_display = self.fishes
        # species = species.capitalize() + "es" if species == "fish" else species.capitalize() + "s"
        # return f"{species} in {self.name}: {', '.join(animals_to_display)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for i in range(count):
    spe, nam = input().split()
    zoo.add_animal(spe, nam)
info = input()
print(zoo.get_info(info))
