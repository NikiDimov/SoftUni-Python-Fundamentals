amount_of_experience = float(input())
battles = int(input())
gathered_experience = 0


def checker(gathered, amount, b):
    if gathered >= amount:
        print(f"Player successfully collected his needed experience for {b} battles.")
        exit()


for battle in range(1, battles + 1):
    gain_experience = float(input())
    gathered_experience += gain_experience
    if battle % 15 == 0:
        gathered_experience += gain_experience * 0.05
        checker(gathered_experience, amount_of_experience, battle)
        continue
    if battle % 3 == 0:
        gathered_experience += gain_experience * 0.15
    if battle % 5 == 0:
        gathered_experience -= gain_experience * 0.1
    checker(gathered_experience, amount_of_experience, battle)
print(f"Player was not able to collect the needed "
      f"experience, {amount_of_experience - gathered_experience:.2f} more needed.")
