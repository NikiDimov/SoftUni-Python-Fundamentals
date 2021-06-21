items = input().split(", ")
text = input()
while not text == "Craft!":
    command, item = text.split(" - ")
    if command == "Collect":
        if item not in items:
            items.append(item)
    elif command == "Drop":
        if item in items:
            items.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items:
            index = items.index(old_item)
            items.insert(index+1, new_item)
    elif command == "Renew":
        if item in items:
            items.append(items.pop(items.index(item)))

    text = input()
print(*items, sep=", ")
