n = int(input())

for i in range(ord("a"), ord("a")+n):
    for j in range(ord("a"), ord("a")+n):
        for k in range(ord("a"), ord("a")+n):
            print(f"{chr(i)}{chr(j)}{chr(k)}")

