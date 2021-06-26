from math import ceil
students = int(input())
lectures = int(input())
additional_bonus = int(input())
student_attendances = []
for _ in range(students):
    attendances = int(input())
    student_attendances.append(attendances)
if lectures:
    total_bonus = max(student_attendances) / lectures * (5 + additional_bonus)
else:
    total_bonus = 0
print(f"Max Bonus: {ceil(total_bonus)}.")
if lectures:
    print(f"The student has attended {max(student_attendances)} lectures.")
else:
    print(f"The student has attended {lectures} lectures.")
