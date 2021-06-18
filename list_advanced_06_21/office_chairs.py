rooms = int(input())
counter = 0
enough_chairs = True
for room in range(1, rooms + 1):
    command = input().split()
    chairs = command[0]
    people = int(command[1])
    if len(chairs) < people:
        enough_chairs = False
        print(f"{people-len(chairs)} more chairs needed in room {room}")
    else:
        counter += len(chairs)-people
if enough_chairs:
    print(f"Game On, {counter} free chairs left")
