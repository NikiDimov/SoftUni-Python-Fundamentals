message = input()
instruction = input()
while not instruction == "Reveal":
    is_error = False
    data = instruction.split(":|:")
    if data[0] == "InsertSpace":
        index = int(data[1])
        message = message[:index] + ' ' + message[index:]
    elif data[0] == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message = message + substring[::-1]
        else:
            print("error")
            is_error = True
    elif data[0] == "ChangeAll":
        substring, replacement = data[1], data[2]
        message = message.replace(substring, replacement)
    if not is_error:
        print(message)
    instruction = input()
print(f"You have a new text message: {message}")
