text = input()
new_text = text[0]
for index in range(len(text)):
    if text[index] == new_text:
        continue
    if not text[index] == text[index-1]:
        new_text += text[index]
print(new_text)

