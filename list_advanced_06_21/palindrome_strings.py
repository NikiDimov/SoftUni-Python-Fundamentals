palindrome_string = input().split()
palindrome = input()
result = []
for el in palindrome_string:
    if el == ''.join(reversed(el)):
        result.append(el)
counter_of_the_palindrome = result.count(palindrome)
print(result)
print(f"Found palindrome {counter_of_the_palindrome} times")
