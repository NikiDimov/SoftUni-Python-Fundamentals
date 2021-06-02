n = int(input())
word = input()
first_result = [input()for _ in range(n)]
second_result = [el for el in first_result if word in el]
print(first_result)
print(second_result)

