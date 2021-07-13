command = input()
forces = {}


def is_there(force_user):
    for f, u in forces.items():
        if force_user in u:
            return True


while not command == "Lumpawaroo":
    if " | " in command:
        data = command.split(" | ")
        force, user = data[0], data[1]
        if not is_there(user) and force not in forces:
            forces[force] = [user]
        elif not is_there(user):
            forces[force].append(user)
        elif is_there(user):
            pass

    elif " -> " in command:
        data = command.split(" -> ")
        user, force = data[0], data[1]
        for k, v in forces.items():
            if user in v:
                v.remove(user)
        if force not in forces:
            forces[force] = [user]
        else:
            forces[force].append(user)
        print(f"{user} joins the {force} side!")
    command = input()

forces_count = {k: len(v) for k, v in forces.items() if len(v) > 0}
forces_count = dict(sorted(forces_count.items(), key=lambda x: x[0]))
forces_count = dict(sorted(forces_count.items(), key=lambda x: -x[1]))


for key, value in forces_count.items():
    print(f"Side: {key}, Members: {value}")
    forces[key].sort()
    for el in forces[key]:
        print(f"! {el}")

