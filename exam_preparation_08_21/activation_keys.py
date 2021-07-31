activation_key = input()
command = input()
while not command == 'Generate':
    instructions = command.split(">>>")
    if instructions[0] == "Contains":
        substring = instructions[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instructions[0] == 'Flip':
        start, end = int(instructions[2]), int(instructions[3])
        if instructions[1] == "Upper":
            activation_key = activation_key[:start]+activation_key[start:end].upper()+activation_key[end:]
        elif instructions[1] == "Lower":
            activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
        print(activation_key)
    elif instructions[0] == 'Slice':
        start,end = int(instructions[1]), int(instructions[2])
        activation_key = activation_key[:start]+activation_key[end:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")
