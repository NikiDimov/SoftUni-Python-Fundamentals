n = int(input())
my_pieces = {}
for _ in range(n):
    data = input().split("|")
    piece, composer, key = data[0], data[1], data[2]
    my_pieces[piece] = {"composer": composer, "key": key}
command = input()
while not command == "Stop":
    data = command.split("|")
    if data[0] == "Add":
        piece, composer, key = data[1], data[2], data[3]
        if piece not in my_pieces:
            my_pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif data[0] == "Remove":
        piece = data[1]
        if piece in my_pieces:
            del my_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif data[0] == "ChangeKey":
        piece, new_key = data[1], data[2]
        if piece in my_pieces:
            my_pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
my_pieces = sorted(my_pieces.items(), key=lambda x: (x[0], x[1]["key"]))
for key, value in my_pieces:
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
