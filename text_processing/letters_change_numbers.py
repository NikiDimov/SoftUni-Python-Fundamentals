def number_in_string(string):
    num = string[1:-1]
    return int(num)


text_command = input().split()
result = 0
total_result = 0
for text in text_command:
    if text[0].isupper():
        result = number_in_string(text) / (ord(text[0]) - 64)
    elif text[0].islower():
        result = number_in_string(text) * (ord(text[0]) - 96)
    if text[-1].isupper():
        result = result - (ord(text[-1]) - 64)
    elif text[-1].islower():
        result = result + (ord(text[-1]) - 96)
    total_result += result

print(f"{total_result:.2f}")


