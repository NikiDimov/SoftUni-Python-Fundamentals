factor = int(input())
count = int(input())
result = []
new_factor = factor
for i in range(count):
    result.append(new_factor)
    new_factor += factor
print(result)
