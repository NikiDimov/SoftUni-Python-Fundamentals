names_of_the_gifts = input().split()
command = input()
while not command == "No Money":
    text = command.split()
    if text[0] == "OutOfStock":
        names_of_the_gifts = ['None' if el == text[1] else el for el in names_of_the_gifts]
    elif text[0] == "Required":
        if 0 <= int(text[2]) < len(names_of_the_gifts):
            names_of_the_gifts[int(text[2])] = text[1]
    elif text[0] == "JustInCase":
        names_of_the_gifts[-1] = text[1]
    command = input()
print(' '.join(el for el in names_of_the_gifts if not el == "None"))
