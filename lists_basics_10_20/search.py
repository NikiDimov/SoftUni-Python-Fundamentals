n = int(input())
word = input()
result = []
result_new = []

for i in range(n):
    sentence = input()
    result.append(sentence)
    if word in sentence:
        result_new.append(sentence)
    # for el in sentence.split():
    #     if el == word:
    #         result_new.append(sentence)

print(result)
print(result_new)















