import re

line = input()
emoji_pattern = r'(::|\*\*)[A-Z][a-z]{2,}\1'
threshold_pattern = r'\d'
result_threshold = re.findall(threshold_pattern, line)
cool_threshold = 1
emoji = []
cool_emoji = []
for el in result_threshold:
    cool_threshold *= int(el)
print(f"Cool threshold: {cool_threshold}")
result_emoji = re.finditer(emoji_pattern, line)
for match in result_emoji:
    emoji.append(match.group())
print(f"{len(emoji)} emojis found in the text. The cool ones are:")
for em in emoji:
    result = em[2:-2]
    coolness = 0
    for ch in result:
        coolness += ord(ch)
    if coolness>cool_threshold:
        cool_emoji.append(em)
for e in cool_emoji:
    print(e)