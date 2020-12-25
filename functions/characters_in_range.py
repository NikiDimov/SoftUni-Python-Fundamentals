# def function(char_1, char_2):
#
#     for i in range(ord(char_1) + 1, ord(char_2)):
#         print(chr(i), end=" ")
#
#
# chr_1 = input()
# chr_2 = input()
#
# function(chr_1, chr_2)

def function(char_1, char_2):
    result = ""
    for i in range(ord(char_1) + 1, ord(char_2)):
        result = result + chr(i) + " "
    return result


chr_1 = input()
chr_2 = input()

print(function(chr_1, chr_2))
