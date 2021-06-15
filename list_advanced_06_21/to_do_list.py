note = input()
to_do_list = [0] * 11
while not note == 'End':
    current_note = note.split("-")
    index = int(current_note[0])
    doing = current_note[1]
    to_do_list.pop(index)
    to_do_list.insert(index, doing)
    note = input()
result = [el for el in to_do_list if not el == 0]
print(result)

