import re

command = input().split(":")
names = {}
courses = {}
pattern = r"[a-zA-Z]+"
while not len(command) == 1:
    course = ''.join(re.findall(pattern,command[2]))
    names[command[1]] = command[0]
    courses[command[1]] = course
    command = input().split(":")
command = ''.join(re.findall(pattern, command[0]))
for key, value in names.items():
    if courses[key] == command:
        print(f"{value} - {key}")


