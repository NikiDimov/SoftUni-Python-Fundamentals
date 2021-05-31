N = int(input())
data_snowballs = {}
for _ in range(N):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    data_snowballs[snowball_value] = [snowball_snow, snowball_time, snowball_quality]
result = max(data_snowballs)
print(f"{data_snowballs[result][0]} : {data_snowballs[result][1]} = {int(result)} ({data_snowballs[result][2]})")
