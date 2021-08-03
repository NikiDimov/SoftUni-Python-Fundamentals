line = input()
command = input()
while not command == 'Done':
    data = command.split()
    if data[0] == 'TakeOdd':
        line = line[1::2]
        print(line)
    elif data[0] == 'Cut':
        index, length = int(data[1]), int(data[2])
        line = line.replace(line[index:index + length], '', 1)
        print(line)
    elif data[0] == 'Substitute':
        substring, substitute = data[1], data[2]
        if substring in line:
            line = line.replace(substring, substitute)
            print(line)
        else:
            print('Nothing to replace!')
    command = input()
print(f"Your password is: {line}")
