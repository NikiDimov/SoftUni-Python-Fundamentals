n = int(input())
dict_pieces = {}
for _ in range(n):
    current_piece = input().split("|")
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    dict_pieces[piece] = {"composer": composer, "key": key}
line = input()
while not line == "Stop":
    command = line.split("|")
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece in dict_pieces:
            print(f"{piece} is already in the collection!")
        else:
            dict_pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        if piece in dict_pieces:
            del dict_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        new_key = command[2]
        if piece in dict_pieces:
            dict_pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    line = input()

sorted_dict_pieces = dict(sorted(dict_pieces.items(),key=lambda x:(x[0],x[1]["composer"])))
for key, value in sorted_dict_pieces.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
