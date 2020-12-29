course = input()
dict_course = {}

while not course == "end":
    course_name, student_name = course.split(" : ")
    if course_name not in dict_course:
        dict_course[course_name] = [1, []]
        dict_course[course_name][1].append(student_name)
    else:
        dict_course[course_name][1].append(student_name)
        dict_course[course_name][0] = len(dict_course[course_name][1])
    dict_course[course_name][1].sort()

    course = input()

dict_course = dict(sorted(dict_course.items(), key=lambda x: x[1][0], reverse=True))
for key, value in dict_course.items():
    print(f"{key}: {value[0]}")
    for name in value[1]:
        print(f"-- {name}")
