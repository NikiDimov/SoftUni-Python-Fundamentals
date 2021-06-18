secret_message = input().split()
decipher_message = []
for text in secret_message:
    first_half = ""
    second_half = []
    for el in text:
        if el.isdigit():
            first_half += el
        else:
            second_half.append(el)
    second_half[0], second_half[-1] = second_half[-1], second_half[0]
    result = chr(int(first_half))+''.join(second_half)
    decipher_message.append(result)
print(' '.join(decipher_message))


