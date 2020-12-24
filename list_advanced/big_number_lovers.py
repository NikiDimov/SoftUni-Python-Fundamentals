numbers_line = input().split()
numbers_line.sort()
numbers_line.reverse()
for el in numbers_line:
    print(f"{el}", end="")
    