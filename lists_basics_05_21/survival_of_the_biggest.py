list1 = [int(el) for el in input().split()]
cycles = int(input())
for _ in range(cycles):
    list1.remove(min(list1))
print(', '.join(map(str, list1)))

