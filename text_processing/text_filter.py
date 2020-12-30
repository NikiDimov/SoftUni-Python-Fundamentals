ban_list = input().split(", ")
text = input()
for el in ban_list:
    if el in text:
        text = text.replace(el, len(el) * "*")
print(text)

