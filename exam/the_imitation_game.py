encrypted_message = input()
line = input()

while not line == "Decode":
    command = line.split("|")
    if command[0] == "Move":
        n_letters = int(command[1])
        encrypted_message = encrypted_message[n_letters:] + encrypted_message[:n_letters]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    line = input()
print(f"The decrypted message is: {encrypted_message}")
