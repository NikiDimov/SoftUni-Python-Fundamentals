line = input().split(", ")
for word in line:
    is_valid = True
    if len(word) in range(3, 17):
        for ch in word:
            if not ch.isalnum() and ch != '-' and ch != '_':
                is_valid = False
                break
        if is_valid:
            print(word)

# With Regex
# import re
# line = input()
# pattern = r'(^|(?<=, ))[\w-]{3,16}($|(?=,))'
# result = re.finditer(pattern, line)
# for el in result:
#     print(el.group())
