import re
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
n = int(input())
counter = 0
result = ""
while not counter >= n:
    barcode = input()
    if not re.match(pattern, barcode):
        print("Invalid barcode")
    else:
        for el in barcode:
            if el.isdigit():
                result += el
        if not result == "":
            print(f"Product group: {result}")
            result = ""
        else:
            print("Product group: 00")
    counter += 1



