list_of_numbers = input().split(", ")
list_of_numbers_in_ints = [int(el) for el in list_of_numbers]
group = []
bound = 10
while not len(list_of_numbers_in_ints) == 0:
    for el in list_of_numbers_in_ints.copy():
        if el <= bound:
            group.append(el)
            list_of_numbers_in_ints.remove(el)
    print(f"Group of {bound}'s: {group}")
    bound += 10
    group = []
