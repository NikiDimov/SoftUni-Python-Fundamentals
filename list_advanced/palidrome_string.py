data = input().split()
searched_word = input()

new_list = [word for word in data if word == word[::-1]]

print(new_list)
occurrences = new_list.count(searched_word)
print(f"Found palindrome {occurrences} times")
