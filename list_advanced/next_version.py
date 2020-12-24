current_version = input().split(".")

result = ""
for el in current_version:
    result += el
result = int(result) + 1
output = []
if result <= 999:
    result = str(result)
    for el in result:
        output.append(el)
output_final = ".".join([str(elem) for elem in output])
print(output_final)
