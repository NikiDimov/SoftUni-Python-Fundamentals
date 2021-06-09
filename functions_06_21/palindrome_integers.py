num_list = input().split(", ")


def palindrome_checker():
    results = []
    for el in num_list:
        is_palindrome = True
        for i in range(len(el) // 2):
            if not el[i] == el[-1 - i]:
                results.append(False)
                is_palindrome = False
                break
        if is_palindrome:
            results.append(True)
    return results


print('\n'.join(map(str, palindrome_checker())))
