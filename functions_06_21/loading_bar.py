num = int(input())


def loading_bar(n):
    full = '%' * (n // 10)
    empty = '.' * (10 - n // 10)
    if n < 100:
        return f"{n}% [{full + empty}]\nStill loading..."
    return f"{n}% Complete!\n[{full + empty}]"


print(loading_bar(num))
