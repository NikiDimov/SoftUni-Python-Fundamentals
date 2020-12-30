# import re
#
# text = input().upper()
# pattern = r"(\D+)(\d+)"
# result = re.findall(pattern, text)
# rage_message = ""
#
# for el in result:
#     rage_message += el[0]*int(el[1])
# unique_symbols = set(rage_message)
# print(f"Unique symbols used: {len(unique_symbols)}")
# print(rage_message)

line = input()
current_result = ''
result = ''
index = 0

while index < len(line):
    if not line[index].isdigit():
        current_result += line[index]
        index += 1
    else:
        number = ''
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1
        number = int(number)
        current_result = current_result.upper()*number
        result += current_result
        current_result = ""
print(f"Unique symbols used: {len(set(result))}")
print(result)







