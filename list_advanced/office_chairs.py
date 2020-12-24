rooms = int(input())
total_free_chairs = 0
needed_chairs = 0
counter = 0
for room in range(1, rooms+1):
    chairs, taken_places = input().split()
    taken_places = int(taken_places)
    if len(chairs) >= taken_places:
        dif = len(chairs) - taken_places
        total_free_chairs += dif
        counter += 1
    else:
        dif = taken_places - len(chairs)
        print(f"{dif} more chairs needed in room {room}")

if counter == rooms:
    print(f"Game On, {total_free_chairs} free chairs left")
