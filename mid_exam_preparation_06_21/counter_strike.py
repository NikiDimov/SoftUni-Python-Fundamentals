energy = int(input())
distance = input()
wins_counter = 0
lost_game = False
while not distance == "End of battle":
    distance = int(distance)
    if energy < distance:
        print(f"Not enough energy! Game ends with {wins_counter} won battles and {energy} energy")
        lost_game = True
        break
    energy -= distance
    wins_counter +=1
    if wins_counter % 3 == 0:
        energy += wins_counter
    distance = input()
if not lost_game:
    print(f"Won battles: {wins_counter}. Energy left: {energy}")
