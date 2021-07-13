courses = {}
command = input()
while not command == "end":
    data = command.split(" : ")
    course_name, student = data[0], data[1]
    if course_name not in courses:
        courses[course_name] = [student]
    else:
        courses[course_name].append(student)
        courses[course_name] = sorted(courses[course_name])
    command = input()

courses_count_students = {k: len(v) for k, v in courses.items()}
courses_count_students = dict(sorted(courses_count_students.items(), key=lambda x: -x[1]))

for key, value in courses_count_students.items():
    print(f"{key}: {value}")
    for name in courses[key]:
        print(f"-- {name}")


