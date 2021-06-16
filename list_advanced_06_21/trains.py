wagon = [0 for _ in range(int(input()))]
command = input()
while not command == 'End':
    command_line = command.split()
    if command_line[0] == 'add':
        wagon[-1] += int(command_line[1])
    elif command_line[0] == 'insert':
        wagon[int(command_line[1])] += int(command_line[2])
    elif command_line[0] == 'leave':
        wagon[int(command_line[1])] -= int(command_line[2])
    command = input()
print(wagon)
