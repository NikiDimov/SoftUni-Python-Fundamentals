username = input()
command = input()
while not command == "Registration":
    data = command.split()
    if data[0] == "Letters":
        if data[1] == "Lower":
            username = username.lower()
        elif data[1] == "Upper":
            username = username.upper()
        print(username)
    elif data[0] == "Reverse":
        start_index, end_index = int(data[1]), int(data[2])
        if start_index < len(username) and end_index < len(username):
            substring = username[start_index:end_index+1]
            print(substring[::-1])
    elif data[0] == "Substring":
        substring = data[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif data[0] == "Replace":
        char = data[1]
        if char in username:
            username = username.replace(char, '-')
            print(username)
    elif data[0] == "IsValid":
        char = data[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
    command = input()