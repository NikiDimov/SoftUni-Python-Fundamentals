line = input()
command = input().split()
password = line
while not command == ["Done"]:
    if command == ["TakeOdd"]:
        new_password = ""
        for i in range(1, len(password), 2):
            new_password += password[i]
        password = new_password
        print(password)
    elif command[0] == "Cut":
        index, length = command[1], command[2]
        index = int(index)
        length = int(length)
        password = password[:index] + password[(index + length):]
        print(password)
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input().split()
print(f"Your password is: {password}")

