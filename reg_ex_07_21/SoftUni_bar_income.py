import re

pattern = r'%(?P<name>[A-Z][a-z]+)%([^\|\$\.\%]*)<(?P<product>\w+)>([^\|\$\.\%]*)\|(?P<count>\d+)\|([^\|\$\.\%]*?)(?P<price>\d+\.?\d+)\$'
line = input()
total_income = 0
while not line == "end of shift":
    result = re.findall(pattern, line)
    if result:
        result = re.finditer(pattern, line)
        for match in result:
            total_price = int(match.group('count')) * float(match.group('price'))
            total_income += total_price
            print(f"{match.group('name')}: {match.group('product')} - {total_price:.2f}")
    line = input()
print(f"Total income: {total_income:.2f}")