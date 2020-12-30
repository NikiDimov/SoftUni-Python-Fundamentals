text = input()
strength = 0
new_text = []
for el in text:
    if el.isalpha() and strength > 0:
        new_text.append(el)
        new_text.pop()
        strength -= 1

    elif el.isdigit():
        strength += int(el)
        new_text.append(el)
        new_text.pop()
        strength -= 1
    else:
        new_text.append(el)
print(''.join(new_text))
