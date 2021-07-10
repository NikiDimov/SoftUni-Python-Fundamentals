cards = input().split(":")
command = input()
new_deck = []
while not command == "Ready":
    data = command.split()
    if data[0] == "Add":
        card_name = data[1]
        if card_name in cards:
            new_deck.append(card_name)
            cards.remove(card_name)
        else:
            print("Card not found.")
    elif data[0] == "Insert":
        card_name, index = data[1], int(data[2])
        if card_name not in cards or index not in range(0, len(new_deck)):
            print("Error!")
        else:
            new_deck.insert(index, card_name)
            cards.remove(card_name)
    elif data[0] == "Remove":
        card_name = data[1]
        if card_name not in new_deck:
            print("Card not found.")
        else:
            new_deck.remove(card_name)
    elif data[0] == "Swap":
        card_name1, card_name2 = data[1], data[2]
        index1 = new_deck.index(card_name1)
        index2 = new_deck.index(card_name2)
        new_deck[index1], new_deck[index2] = new_deck[index2], new_deck[index1]
    elif data[0] == "Shuffle":
        new_deck = new_deck[::-1]
    command = input()
print(*new_deck, sep=' ')
