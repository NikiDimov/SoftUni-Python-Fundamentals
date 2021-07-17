line = input()
while not line == 'end':
    print(f'{line} = {line[::-1]}')
    line = input()
