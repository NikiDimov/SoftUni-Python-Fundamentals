class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
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
        self.__animals += 1

    def get_info(self, species):
        result = ''
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {self.__animals}"
        return result


name_zoo = input()
zoo = Zoo(name_zoo)
n = int(input())
for _ in range(n):
    command = input()
    curr_species, curr_name = command.split()
    zoo.add_animal(curr_species, curr_name)
info = input()
print(zoo.get_info(info))
