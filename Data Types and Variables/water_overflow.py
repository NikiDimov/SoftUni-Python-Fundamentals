n = int(input())
tank_capacity = 255
current_capacity = 0
for _ in range(n):
    flow = int(input())
    if flow > tank_capacity - current_capacity:
        print("Insufficient capacity!")
        continue
    current_capacity += flow
print(current_capacity)


