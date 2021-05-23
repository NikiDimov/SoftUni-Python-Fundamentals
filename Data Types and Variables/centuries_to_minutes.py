get_century = int(input())
years = get_century * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{get_century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

