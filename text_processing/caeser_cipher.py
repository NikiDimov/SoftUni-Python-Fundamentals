text = input()
cipher = ""
for letter in text:
    cipher += chr(ord(letter) + 3)
print(cipher)



