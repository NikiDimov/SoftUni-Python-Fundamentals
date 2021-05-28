n = int(input())
for x1 in range(n):
    for x2 in range(n):
        for x3 in range(n):
            print(f"{chr(97+x1)}{chr(97+x2)}{chr(97+x3)}")
