year = int(input())
while True:
    happy_year = True
    year += 1
    for d in str(year):
        if str(year).count(d) > 1:
            happy_year = False
            break
    if happy_year:
        print(year)
        break
