number_of_cars = int(input())
my_cars = {}
for _ in range(number_of_cars):
    current_car = input().split("|")
    car = current_car[0]
    mile_age = int(current_car[1])
    fuel = int(current_car[2])
    my_cars[car] = {"mile_age": mile_age, "fuel": fuel}

line = input()
while not line == "Stop":
    command = line.split(" : ")
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > my_cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            my_cars[car]["mile_age"] += distance
            my_cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if my_cars[car]["mile_age"] >= 100000:
                del (my_cars[car])
                print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        fuel = int(command[2])
        if my_cars[car]["fuel"] < 75:
            my_cars[car]["fuel"] += fuel
            if my_cars[car]["fuel"] >= 75:
                fuel = 75 - (my_cars[car]["fuel"] - fuel)
                my_cars[car]["fuel"] = 75
            print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        km = int(command[2])
        my_cars[car]["mile_age"] -= km
        if my_cars[car]["mile_age"] <= 10000:
            my_cars[car]["mile_age"] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

    line = input()

my_cars_sorted = dict(sorted(my_cars.items(), key=lambda x: (-x[1]["mile_age"], x[0])))
for car, value in my_cars_sorted.items():
    print(f"{car} -> Mileage: {value['mile_age']} kms, Fuel in the tank: {value['fuel']} lt.")
