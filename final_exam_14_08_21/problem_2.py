import re
pattern = r'(\*|@)(?P<tag>[A-Z][a-z]{2,})\1: \[(?P<gr_1>[a-zA-Z])\]\|\[(?P<gr_2>[a-zA-Z])\]\|\[(?P<gr_3>[a-zA-Z])\]\|$'
n = int(input())
for _ in range(n):
    line = input()
    result = re.findall(pattern, line)
    if not result:
        print("Valid message not found!")
    else:
        match = re.finditer(pattern, line)
        for m in match:
            print(f"{m.group('tag')}: {ord(m.group('gr_1'))} {ord(m.group('gr_2'))} {ord(m.group('gr_3'))}")
