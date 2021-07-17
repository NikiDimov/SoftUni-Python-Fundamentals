line = input()
digits = ''
letters = ''
other = ''
for ch in line:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch
print(f"{digits}\n{letters}\n{other}")
