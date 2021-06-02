n = int(input())
list1 = [int(input()) for _ in range(n)]
filters = input()
if filters == "even":
    print([el for el in list1 if el % 2 == 0])
elif filters == "odd":
    print([el for el in list1 if not el % 2 == 0])
elif filters == "negative":
    print([el for el in list1 if el < 0])
elif filters == "positive":
    print([el for el in list1 if el >= 0])

