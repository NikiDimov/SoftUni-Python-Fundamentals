list_to_modify = [int(el) for el in input().split()]
text = input()
while not text == 'end':
    command = text.split()
    if command[0] == 'swap':
        index1, index2 = int(command[1]), int(command[2])
        list_to_modify[index1], list_to_modify[index2] = list_to_modify[index2], list_to_modify[index1]
    elif command[0] == 'multiply':
        index1, index2 = int(command[1]), int(command[2])
        list_to_modify[index1] *= list_to_modify[index2]
    elif command[0] == 'decrease':
        list_to_modify = [el-1 for el in list_to_modify]
    text = input()
print(*list_to_modify, sep=", ")
