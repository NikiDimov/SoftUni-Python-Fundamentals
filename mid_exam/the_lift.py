people = int(input())
lift = input().split()
lift = [int(el) for el in lift]
new_lift = []
waiting_people = people
for el in lift:
    if el <= 4 and people > 4:
        new_lift.append(4)
    else:
        new_lift.append(people)
    people = people - (4 - el)

if len(new_lift) * 4 > sum(new_lift):
    print(f"The lift has empty spots!\n{' '.join(map(str, new_lift))}")
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!\n{' '.join(map(str, new_lift))}")
if people == 0 and len(new_lift)*4 == sum(new_lift):
    print(f"{' '.join(map(str, new_lift))}")
