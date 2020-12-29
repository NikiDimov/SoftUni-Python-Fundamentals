n = int(input())
students = {}
classified_students = {}

for index in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [1, []]
        students[name][1].append(grade)
    else:
        students[name][1].append(grade)
        students[name][0] = len(students[name][1])
for name in students:
    average_grade = sum(students[name][1]) / students[name][0]
    if average_grade >= 4.5:
        classified_students[name] = average_grade
classified_students = sorted(classified_students.items(), key=lambda x: x[1], reverse=True)

for name, grade in classified_students:
    print(f"{name} -> {grade:.2f}")
