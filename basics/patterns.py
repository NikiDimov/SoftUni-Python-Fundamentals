n = int(input())
for row in range(1, n + 1):
    print("*" * row)
for row in range(1, n):
    print("*" * (n - 1))
    n -= 1
