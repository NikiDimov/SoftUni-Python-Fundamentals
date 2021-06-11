password = input()


def length_checker():
    if len(password) not in range(6, 11):
        return "Password must be between 6 and 10 characters"
    return True


def consistence():
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return "Password must consist only of letters and digits"
    return True


def check_for_two_digits():
    counter_digits = 0
    for char in password:
        if char.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        return "Password must have at least 2 digits"
    return True


def password_checker(password):
    is_valid = True
    if not length_checker() is True:
        print(length_checker())
        is_valid = False
    if not consistence() is True:
        print(consistence())
        is_valid = False
    if not check_for_two_digits() is True:
        print(check_for_two_digits())
        is_valid = False
    if is_valid:
        print("Password is valid")


password_checker(password)
