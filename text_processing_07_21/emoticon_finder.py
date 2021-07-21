line = input()
result = [line[i] + line[i+1]for i in range(len(line)) if line[i] == ':']
print('\n'.join(result))