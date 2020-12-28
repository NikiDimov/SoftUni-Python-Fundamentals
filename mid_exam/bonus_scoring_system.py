students = int(input())
lectures = int(input())
bonus = int(input())
bonus_points_list = []
for count in range(students):
    count_of_attendances = int(input())
    total_bonus = count_of_attendances/lectures*(5+bonus)
    bonus_points_list.append(round(total_bonus))
max_bonus_point = max(bonus_points_list)
print(f"Max Bonus: {round(max_bonus_point)}.")
print(f"The student has attended {round((max_bonus_point / (5 + bonus)) * lectures)} lectures.")



