number_of_people = int(input())
capacity_of_elevator = int(input())
total_courses = 0
if number_of_people > capacity_of_elevator:
    total_courses += number_of_people // capacity_of_elevator
    if not number_of_people % capacity_of_elevator == 0:
        total_courses += 1
else:
    total_courses += 1
print(total_courses)
