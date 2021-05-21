enter_age = int(input())
print("drink", end=' ')
if enter_age <= 14:
    print("toddy")
elif enter_age <= 18:
    print("coke")
elif enter_age <= 21:
    print("beer")
else:
    print("whisky")
