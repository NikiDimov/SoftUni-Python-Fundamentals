message = input()
command = input()
while not command == "Decode":
    data = command.split("|")
    if data[0] == "Move":
        nums = int(data[1])
        message = message[nums:]+message[:nums]
    elif data[0] == "Insert":
        index, value = int(data[1]), data[2]
        message = message[:index] + value + message[index:]
    elif data[0] == "ChangeAll":
        substring, replacement = data[1], data[2]
        message = message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {message}")
