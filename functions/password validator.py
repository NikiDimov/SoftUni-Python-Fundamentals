def function(password):
    counter_digits = 0
    counter_symbols = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    for char in password:
        if 1 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 127:
            counter_symbols += 1
        elif 48 <= ord(char) <= 57:
            counter_digits += 1
    if counter_symbols > 0:
        print("Password must consist only of letters and digits")
    if counter_digits < 2:
        print("Password must have at least 2 digits")
    if counter_digits >= 2 and counter_symbols == 0 and 6 <= len(password) <= 10:
        print("Password is valid")


input_password = input()
function(input_password)
