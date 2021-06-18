first_line = input().split(", ")
second_line = input().split(", ")
result = []

for str1 in first_line:
    for str2 in second_line:
        if str1 in str2 and str1 not in result:
            result.append(str1)
print(result)
