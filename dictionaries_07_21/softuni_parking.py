n = int(input())
registered_cars = {}
for _ in range(n):
    command = input().split()
    if command[0] == "register":
        user, number = command[1], command[2]
        if user not in registered_cars:
            registered_cars[user] = number
            print(f"{user} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")
    elif command[0] == "unregister":
        user = command[1]
        if user not in registered_cars:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            del registered_cars[user]

for key, value in registered_cars.items():
    print(f"{key} => {value}")


