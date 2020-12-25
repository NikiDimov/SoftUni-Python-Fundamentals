def loading_bar(number):
    percent = number // 10
    if not number == 100:
        print(str(number) + "% [" + "%" * percent + "." * (10 - percent) + "]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[" + "%" * percent + "]")


num = int(input())
loading_bar(num)
