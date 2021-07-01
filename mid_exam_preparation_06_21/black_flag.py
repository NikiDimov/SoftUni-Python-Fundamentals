days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())
total_plunder = 0
additional_plunder = plunder_per_day*0.5
for day in range(1,days+1):
    total_plunder+=plunder_per_day
    if day % 3 == 0:
        total_plunder+=additional_plunder
    if day % 5 == 0:
        total_plunder = total_plunder - total_plunder*0.3
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder/expected_plunder*100:.2f}% of the plunder.")
