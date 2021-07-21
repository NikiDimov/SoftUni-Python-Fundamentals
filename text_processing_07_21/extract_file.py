# with regex
import re

line = input()
pattern = r'(?P<file_name>((?<=\\)[\w\d\s-]+))(?P<point>[.])(?P<extension>[a-z]+)'
result = re.finditer(pattern, line)
for el in result:
    print(f"File name: {el.group('file_name')}\nFile extension: {el.group('extension')}")
