n = int(input())
my_dict = {}
for _ in range(n):
    key = input()
    value = input()
    if key not in my_dict:
        my_dict[key]=[value]
    else:
        my_dict[key].append(value)
for key, value in my_dict.items():
    print(f"{key} - {', '.join(value)}")

