n = int(input())
students = {}
for _ in range(n):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)
filtered_students = {k: sum(v) / len(v) for k, v in students.items() if sum(v) / len(v) >= 4.5}
filtered_students = dict(sorted(filtered_students.items(), key=lambda x: -x[1]))
for key, value in filtered_students.items():
    print(f"{key} -> {value:.2f}")

