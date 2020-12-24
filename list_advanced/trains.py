wagons = int(input())
train = [0 for _ in range(wagons)]
command = input()
while not command == "End":
    data = command.split()
    if data[0] == "add":
        people = int(data[1])
        train[-1] += people
    elif data[0] == "insert":
        index = int(data[1])
        people = int(data[2])
        train[index] += people
    elif data[0] == "leave":
        index = int(data[1])
        people = int(data[2])
        train[index] -= people
    command = input()
print(train)
