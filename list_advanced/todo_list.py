todo_notes = input()
todo_list = [0 for num in range(10)]
while not todo_notes == "End":
    data = todo_notes.split("-")
    importance = int(data[0])
    value = data[1]
    todo_list.insert(importance, value)
    todo_notes = input()
result = [el for el in todo_list if not el == 0]
print(result)
