card = input()
result = card.split()
players_A_count = 0
players_B_count = 0

for el in set(result):
    if el[0] == "A":
        players_A_count += 1
    elif el[0] == "B":
        players_B_count += 1

print(f"Team A - {(11 - players_A_count)}; Team B - {(11 - players_B_count)}")

if players_A_count > 4 or players_B_count > 4:
    print("Game was terminated")

