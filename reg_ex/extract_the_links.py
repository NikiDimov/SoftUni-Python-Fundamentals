import re
text = input()
pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"
while text:
    emails = re.finditer(pattern, text)
    for mail in emails:
        print(mail.group())
    text = input()


