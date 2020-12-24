neighbourhood = input().split("@")
neighbourhood = [int(el) for el in neighbourhood]
command = input()
position = 0
counter = 0

while not command == "Love!":
    jump, length = command.split()
    length = int(length)
    if jump == "Jump":
        position += length
        if position > len(neighbourhood) - 1:
            position = 0
        if position <= len(neighbourhood) - 1:
            neighbourhood[position] -= 2
            if neighbourhood[position] == 0:
                print(f"Place {position} has Valentine's day.")
            elif neighbourhood[position] < 0:
                print(f"Place {position} already had Valentine's day.")
                neighbourhood[position] = 0

    command = input()
print(f"Cupid's last position was {position}.")

for el in neighbourhood:
    if not el == 0:
        counter += 1
if counter > 0:
    print(f"Cupid has failed {counter} places.")
else:
    print("Mission was successful.")

