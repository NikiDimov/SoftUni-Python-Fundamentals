divisor = int(input())
bound = int(input())

for N in range(bound, 1, -1):
    if N % divisor == 0:
        print(N)
        break

