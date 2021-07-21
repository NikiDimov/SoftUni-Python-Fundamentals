line = input()


def encryption(line):
    encr = ''
    for char in line:
        encr += chr(ord(char) + 3)
    return encr


print(encryption(line))
