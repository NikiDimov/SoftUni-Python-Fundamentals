secret_message = input().split()
output = []
for word in secret_message:
    current_int = []
    sum_int = ''
    sum_letter = ''
    for letter in word:
        if 48 <= ord(letter) <= 57:
            current_int.append(letter)
            sum_int += letter
        else:
            sum_letter += letter
    if len(sum_letter) > 1:
        result = chr(int(sum_int)) + sum_letter[-1:] + sum_letter[1:-1] + sum_letter[:1]
        output.append(result)
    else:
        result = chr(int(sum_int)) + sum_letter
        output.append(result)
list_to_string = ' '.join([str(el) for el in output])
print(list_to_string)
