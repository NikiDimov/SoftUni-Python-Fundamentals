# version I
import re

pattern = r"(:{2}|\*{2})[A-Z][a-z]{2,}\1"
pattern_digits = r"\d"
line = input()
emoji = []
threshold = 1
match = re.finditer(pattern, line)
for el in match:
    emoji.append(el.group())
match_d = re.finditer(pattern_digits, line)
for el in match_d:
    threshold *= int(el.group())
print(f"Cool threshold: {threshold}")
print(f"{len(emoji)} emojis found in the text. The cool ones are:")
for el in emoji:
    sum_ascii = 0
    for symbol in el:
        if symbol.isalpha():
            sum_ascii += ord(symbol)
    if sum_ascii > threshold:
        print(el)

# version II

# import re
#
# text = input()
# pattern = r"(:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1"
# cool_threshold = 1
# numbers = re.findall(r"\d", text)
# for n in range(len(numbers)):
#     cool_threshold *= int(numbers[n])
# emojis_dict = {}
# emojis = re.finditer(pattern, text)
# for emoji in emojis:
#     emoji_value = 0
#     e = emoji.group()
#     for char in e:
#         if char.isalpha():
#             emoji_value += ord(char)
#     emojis_dict[e] = emoji_value
# print(f"Cool threshold: {cool_threshold}")
# print(f"{len(emojis_dict)} emojis found in the text. The cool ones are:")
# for el in emojis_dict:
#     if emojis_dict[el] > cool_threshold:
#         print(el)
