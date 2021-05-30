n = int(input())
brackets = []
result = True
for _ in range(n):
    current_char = input()
    if current_char == "(" or current_char == ")":
        brackets.append(current_char)
if len(brackets) % 2 == 1:
    print("UNBALANCED")
    exit(0)
for i in range(len(brackets)):
    if i % 2 == 0 and brackets[i] == "(":
        continue
    elif i % 2 == 1 and brackets[i] == ")":
        continue
    else:
        print("UNBALANCED")
        result = False
        break
if result:
    print("BALANCED")
