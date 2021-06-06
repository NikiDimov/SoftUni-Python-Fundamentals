line = [int(el)for el in input().split(", ")]
beggars = int(input())
result = []
for beggar in range(1, beggars+1):
    counter = 0
    for i in range(beggar-1, len(line), beggars):
        counter += line[i]
    result.append(counter)
print(result)

