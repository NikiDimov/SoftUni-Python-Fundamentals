import re


def letter_position(letter):
    position = ord(letter.lower()) - 96
    return position


line = input()
pattern = r'(?P<first_letter>[a-zA-Z])(?P<number>[\d]+)(?P<second_letter>[a-zA-Z])'
total_result = 0
result = re.finditer(pattern, line)
for text in result:
    current_result = 0
    a = text.group('first_letter')
    num = text.group('number')
    b = text.group('second_letter')
    if a.isupper():
        current_result += int(num) / letter_position(a)
    elif a.islower():
        current_result += int(num) * letter_position(a)
    if b.isupper():
        current_result -= letter_position(b)
    elif b.islower():
        current_result += letter_position(b)
    total_result += current_result
print(f"{total_result:.2f}")
