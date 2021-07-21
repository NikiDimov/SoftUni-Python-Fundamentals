line = input()
result = ''
for i in range(len(line)):
    result += line[i]
    try:
        while line[i] == line[i + 1]:
            line = line.replace(line[i], '', 1)
    except(BaseException):
        break
print(result)
