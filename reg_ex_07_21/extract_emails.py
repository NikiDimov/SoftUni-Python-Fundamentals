import re

pattern = r'(?P<user>(^|(?<= ))[a-zA-Z0-9]+[.\-_]?[a-zA-Z0-9]+)@' \
          r'(?P<host>([a-zA-Z]+\-?[a-zA-Z]+\.)+[a-zA-Z]+\-?[a-zA-Z]+)'
line = input()
result = re.finditer(pattern, line)
for match in result:
    print(f"{match.group('user')}@{match.group('host')}")
