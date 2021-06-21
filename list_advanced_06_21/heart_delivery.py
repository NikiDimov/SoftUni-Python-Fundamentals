neighbourhood = [int(el) for el in input().split("@")]
command = input()
current_pos = 0
mission_success = True


def checker(pos):
    if neighbourhood[pos] == 0:
        print(f"Place {pos} already had Valentine's day.")
        return
    neighbourhood[pos] -= 2
    if neighbourhood[pos] == 0:
        print(f"Place {pos} has Valentine's day.")


while not command == "Love!":
    jump = command.split()
    length = int(jump[1])
    current_pos += length
    if not current_pos >= len(neighbourhood):
        checker(current_pos)
    else:
        current_pos = 0
        checker(current_pos)
    command = input()
print(f"Cupid's last position was {current_pos}.")

for el in neighbourhood:
    if not el == 0:
        a = neighbourhood.count(0)
        print(f"Cupid has failed {len(neighbourhood) - a} places.")
        mission_success = False
        break
if mission_success:
    print(f"Mission was successful.")
