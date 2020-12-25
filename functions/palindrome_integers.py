# pal = input().split(", ")
#
#
# def function(palindrome):
#
#     for el in palindrome:
#         counter = 0
#         for i in range(0, ((len(el)) // 2)):
#             if not el[i] == el[-1 - i]:
#                 print("False")
#                 break
#             counter += 1
#         if counter == len(el) // 2:
#             print("True")
#
#
# function(pal)

def is_palindrome(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    return False


def separate_elements(text, sep):
    numbers_as_string = text.split(sep)
    return numbers_as_string


data = input()
nums_strings = separate_elements(data, ", ")

for el in nums_strings:
    print(is_palindrome(el))
