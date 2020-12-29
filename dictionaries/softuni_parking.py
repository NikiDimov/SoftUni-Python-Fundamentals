n = int(input())
registered_plates = {}
for index in range(n):
    command = input().split()
    if command[0] == "register":
        if command[1] not in registered_plates:
            registered_plates[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[2]}")
    elif command[0] == "unregister":
        if command[1] in registered_plates:
            registered_plates.pop(command[1])
            print(f"{command[1]} unregistered successfully")
        else:
            print(f"ERROR: user {command[1]} not found")
for name, number in registered_plates.items():
    print(f"{name} => {number}")
