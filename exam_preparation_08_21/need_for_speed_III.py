n = int(input())
my_cars = {}
TANK_CAPACITY = 75
for _ in range(n):
    car_data = input().split("|")
    car, mileage, fuel = car_data[0], int(car_data[1]), int(car_data[2])
    my_cars[car] = [mileage, fuel]
command = input()
while not command == "Stop":
    data = command.split(" : ")
    if data[0] == "Drive":
        car, distance, fuel = data[1], int(data[2]), int(data[3])
        if not fuel > my_cars[car][1]:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            my_cars[car][0] += distance
            my_cars[car][1] -= fuel
            if my_cars[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del my_cars[car]
        else:
            print("Not enough fuel to make that ride")
    elif data[0] == "Refuel":
        car, fuel = data[1], int(data[2])
        if my_cars[car][1] + fuel > TANK_CAPACITY:
            amount = TANK_CAPACITY - my_cars[car][1]
            my_cars[car][1] = TANK_CAPACITY
        else:
            amount = fuel
            my_cars[car][1] += fuel
        print(f"{car} refueled with {amount} liters")
    elif data[0] == "Revert":
        car, kilometers = data[1], int(data[2])
        if my_cars[car][0] - kilometers < 10000:
            my_cars[car][0] = 10000
        else:
            my_cars[car][0] -= kilometers
            amount_reverted = kilometers
            print(f"{car} mileage decreased by {amount_reverted} kilometers")

    command = input()
my_cars = dict(sorted(my_cars.items(), key=lambda x: (-x[1][0], x[0])))
for key, value in my_cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
