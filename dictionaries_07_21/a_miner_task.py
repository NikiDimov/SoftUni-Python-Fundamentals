my_dict = {}
while True:
    key = input()
    if key == 'stop':
        break
    value = input()
    if key not in my_dict:
        my_dict[key]=int(value)
    else:
        my_dict[key]+=int(value)

for key, value in my_dict.items():
    print(f"{key} -> {value}")



