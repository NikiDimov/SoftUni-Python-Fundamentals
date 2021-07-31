import re

pattern = r'(?P<sub_domain>www)\.(?P<domain_name>[a-zA-Z0-9-]+)\.(?P<domain_extension>[a-z]+((\.[a-z]+)+)?)'
line = input()
while line:
    result = re.finditer(pattern, line)
    for match in result:
        print(f"{match.group('sub_domain')}.{match.group('domain_name')}.{match.group('domain_extension')}")
    line = input()