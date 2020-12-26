class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        result = ''
        if money >= self.price and self.owner is None:
            result = f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
            self.owner = owner
        elif money < self.price and self.owner is None:
            result = f"Sorry, not enough money"
        elif self.owner is not None:
            result = f"Car already sold"
        return result

    def sell(self):
        if self.owner is not None:
            self.owner = None

        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            result = f"{self.model} {self.type} is on sale: {self.price}"
        return result


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

