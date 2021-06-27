initial_list = input().split("!")
command = input()
while not command == "Go Shopping!":
    text = command.split()
    if text[0] == "Urgent":
        item = text[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif text[0] == "Unnecessary":
        item = text[1]
        if item in initial_list:
            initial_list.remove(item)
    elif text[0] == "Correct":
        old_item, new_item = text[1], text[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item
    elif text[0] == "Rearrange":
        item = text[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input()
print(*initial_list, sep=", ")