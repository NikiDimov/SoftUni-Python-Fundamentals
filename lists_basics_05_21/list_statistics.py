n = int(input())
list1 = [int(input()) for _ in range(n)]
positives = []
negatives = []
[positives.append(el) if el >= 0 else negatives.append(el) for el in list1]
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")
