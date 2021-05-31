key = int(input())
lines = int(input())
for _ in range(lines):
    letter = input()
    result = ord(letter)+key
    print(f"{chr(result)}", end="")

