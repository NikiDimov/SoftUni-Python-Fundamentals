import re

n = int(input())
pattern = r'@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+'
d_pattern = r'\d'
for _ in range(n):
    barcode = input()
    if re.findall(pattern, barcode):
        if re.findall(d_pattern, barcode):
            group = re.findall(d_pattern, barcode)
            print(f"Product group: {''.join(group)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
