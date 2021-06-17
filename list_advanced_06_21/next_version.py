current_version = input().split(".")
next_version = ''
for el in current_version:
    next_version += el
print('.'.join(list(str(int(next_version) + 1))))
