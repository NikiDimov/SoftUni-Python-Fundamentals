sides = {}

command = input()
while not command == "Lumpawaroo":
    text = command.split(" | ")
    text2 = command.split(" -> ")
    if len(text) > len(text2):
        text_command = text
        force_side, force_user = text_command[0], text_command[1]
        if force_side not in sides:
            sides[force_side] = []
        if force_user not in sides[force_side]:
            sides[force_side].append(force_user)
    else:
        text_command = text2
        force_user, force_side = text_command[0], text_command[1]
        for key, value in sides.items():
            if force_user in value:
                if force_user in value:
                    value.remove(force_user)

        if force_side not in sides:
            sides[force_side] = []
            sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            if force_user not in sides[force_side]:
                sides[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")

    command = input()
sides = dict(sorted(sides.items(), key=lambda x:( -len(x[1]), x[0])))
for key, value in sides.items():
    if not value:
        sides.pop(key)
        break
    value.sort()

for key, value in sides.items():
    print(f"Side: {key}, Members: {len(value)}")
    for member in value:
        print(f"! {member}")
