collection = input().split(", ")
command = input()
while not command == "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        if item in collection:
            continue
        else:
            collection.append(item)
    elif action == "Drop":
        if item in collection:
            collection.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collection:
            index = collection.index(old_item)
            collection.insert(index + 1, new_item)
    elif action == "Renew":
        if item in collection:
            collection.remove(item)
            collection.append(item)
    command = input()
print(", ".join(collection))


