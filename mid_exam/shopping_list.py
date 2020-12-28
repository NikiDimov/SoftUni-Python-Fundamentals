initial_list = input().split("!")

command = input()

while command != "Go Shopping!":
    text = command.split()
    if text[0] == "Urgent" and text[1] not in initial_list:
        initial_list.insert(0, text[1])
    if text[0] == "Unnecessary" and text[1] in initial_list:
        initial_list.remove(text[1])
    if text[0] == "Correct" and text[1] in initial_list:
        initial_list = [text[2] if x == text[1] else x for x in initial_list]
    if text[0] == "Rearrange" and text[1] in initial_list:
        initial_list.remove(text[1])
        initial_list.append(text[1])

    command = input()
print(", ".join(initial_list))
