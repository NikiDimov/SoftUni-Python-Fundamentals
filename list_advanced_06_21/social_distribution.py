population = [int(el) for el in input().split(", ")]
min_wealth = int(input())
if sum(population) < len(population) * min_wealth:
    print("No equal distribution possible")
    exit()

for i in range(len(population)):
    if population[i] < min_wealth:
        index = population.index(max(population))
        difference = min_wealth - population[i]
        if population[index] - difference >= min_wealth:
            population[i] += difference
            population[index] -= difference
        else:
            population[i] += population[index] - min_wealth
            population[index] = min_wealth
print(population)

