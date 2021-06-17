numbers = [int(el) for el in input().split(", ")]
print(f"Positive: {', '.join(map(str,([el for el in numbers if el >= 0])))}")
print(f"Negative: {', '.join(map(str,([el for el in numbers if el < 0])))}")
print(f"Even: {', '.join(map(str,([el for el in numbers if el % 2==0])))}")
print(f"Odd: {', '.join(map(str,([el for el in numbers if el % 2==1])))}")
