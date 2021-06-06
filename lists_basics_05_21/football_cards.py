cards = set(input().split())
team_A_counter = 0
team_B_counter = 0
game_is_terminated = False
for card in cards:
    team, *_ = card.split("-")
    if team == "A":
        team_A_counter += 1
    else:
        team_B_counter += 1
    if team_A_counter > 4 or team_B_counter > 4:
        game_is_terminated = True
        break
print(f"Team A - {11 - team_A_counter}; Team B - {11 - team_B_counter}")
if game_is_terminated:
    print(f"Game was terminated")
