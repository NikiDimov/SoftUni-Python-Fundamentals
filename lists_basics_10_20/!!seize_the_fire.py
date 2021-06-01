# fire_data = input().split("#")
# water_amount = int(input())
#
# RANGE_HIGH = range(81, 126)
# RANGE_MEDIUM = range(51, 81)
# RANGE_LOW = range(1, 51)
#
# effort = 0
# put_out_fire = []
#
# for fire in fire_data:
#     type_of_fire, value = fire.split(" = ")
#     value = int(value)
#
#     if type_of_fire == "High" and value not in RANGE_HIGH:
#         continue
#     elif type_of_fire == "Medium" and value not in RANGE_MEDIUM:
#         continue
#     elif type_of_fire == "Low" and value not in RANGE_LOW:
#         continue
#
#     if water_amount >= value:
#         water_amount -= value
#         effort += value*0.25
#         put_out_fire.append(value)
#
# print("Cells:")
# for fire_value in put_out_fire:
#     print(f" - {fire_value}")
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {sum(put_out_fire)}")

level_of_fire = input().split("#")
amount_of_water = int(input())

fire_high = range(81, 126)
fire_medium = range(51, 81)
fire_low = range(1, 51)
effort = 0
put_out_fire = []

for fire in level_of_fire:
    type_of_fire, value = fire.split(" = ")
    value = int(value)
    if type_of_fire == "High" and value not in fire_high:
        continue
    elif type_of_fire == "Medium" and value not in fire_medium:
        continue
    elif type_of_fire == "Low" and value not in fire_low:
        continue

    if value <= amount_of_water:
        amount_of_water -= value
        effort = effort + value*0.25
        put_out_fire.append(value)

print("Cells:")
for fire_value in put_out_fire:
    print(f" - {fire_value}")
print(f"{effort:.2f}")
print(f"Total fire:{sum(put_out_fire)}")








