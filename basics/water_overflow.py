n = int(input())
capacity = 255
current_water = 0
for i in range(1, n + 1):
    quantity = int(input())
    current_water += quantity
    if current_water > capacity:
        print("Insufficient capacity!")
        current_water = current_water - quantity
print(current_water)



