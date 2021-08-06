stops = input()
commands = input()
while not commands == "Travel":
    data = commands.split(":")
    if data[0] == "Add Stop":
        index, string = int(data[1]), data[2]
        if not index >= len(stops):
            stops = stops[:index] + string + stops[index:]
    elif data[0] == "Remove Stop":
        start_index, end_index = int(data[1]), int(data[2])
        if not start_index >= len(stops) and not end_index >= len(stops):
            stops = stops.replace(stops[start_index:end_index + 1], '')
    elif data[0] == "Switch":
        old_string, new_string = data[1], data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    commands = input()
print(f"Ready for world tour! Planned stops: {stops}")
