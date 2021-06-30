people = int(input())
the_lift = [int(wagon) for wagon in input().split()]
for index in range(len(the_lift)):
    current_people = the_lift[index]
    if current_people < 4:
        needed_people = 4 - current_people
        if needed_people <= people:
            the_lift[index] += needed_people
            people -= needed_people
        else:
            the_lift[index] += people
            people = 0
            break
if people == 0 and sum(the_lift) != len(the_lift) * 4:
    print("The lift has empty spots!")
elif people > 0 and sum(the_lift) == len(the_lift) * 4:
    print(f"There isn't enough space! {people} people in a queue!")
print(*the_lift, sep=' ')