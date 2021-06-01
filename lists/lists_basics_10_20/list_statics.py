# n = int(input())
# positive_result = []
# negative_result = []
# count_positives = 0
# sum_negatives = 0
# for i in range(n):
#     num = int(input())
#     if num >= 0:
#         positive_result.append(num)
#         count_positives += 1
#     else:
#         negative_result.append(num)
#         sum_negatives += num
# print(positive_result)
# print(negative_result)
# print(f"Count of positives: {count_positives}."
#       f" Sum of negatives: {sum_negatives}")

n = int(input())
positive_result = []
negative_result = []

for i in range(n):
    num = int(input())
    if num >= 0:
        positive_result.append(num)
    else:
        negative_result.append(num)
print(positive_result)
print(negative_result)
print(f"Count of positives: {len(positive_result)}. Sum of negatives: {sum(negative_result)}")

