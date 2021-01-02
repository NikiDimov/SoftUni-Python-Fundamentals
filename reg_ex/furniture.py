import re

line = input()
pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
names = []
total_price = 0

while not line == "Purchase":
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        names.append(obj["name"])
        total_price += float(obj["price"])*int(obj["quantity"])
    line = input()

print("Bought furniture:")
for f in names:
    print(f)
print(f"Total money spend: {total_price:.2f}")
