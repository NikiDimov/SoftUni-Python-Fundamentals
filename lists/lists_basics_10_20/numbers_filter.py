n = int(input())
odd = []
even = []
negative = []
positive = []
for i in range(n):
    num = int(input())
    if num % 2 == 0 or num == 0:
        even.append(num)
    else:
        odd.append(num)
    if num < 0:
        negative.append(num)
    else:
        positive.append(num)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)


