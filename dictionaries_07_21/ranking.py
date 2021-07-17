contest_line = input()
contest_data = {}
users = {}
while not contest_line == "end of contests":
    contest, password = contest_line.split(":")
    contest_data[contest] = password
    contest_line = input()
submissions = input()
while not submissions == "end of submissions":
    contest, password, username, points = submissions.split("=>")
    points = int(points)
    if contest in contest_data and password == contest_data[contest]:
        if username not in users:
            users[username] = {}
        if contest not in users[username]:
            users[username][contest] = []
        users[username][contest].append(points)

    submissions = input()
for key, value in users.items():
    users[key] = {k: max(v) for k, v in value.items()}
total_points_candidate = {}
for key, value in users.items():
    total_points_candidate[key] = sum(value.values())
max_points = max(total_points_candidate.values())

for key, value in total_points_candidate.items():
    if value == max_points:
        print(f"Best candidate is {key} with total {max_points} points.\n"
              f"Ranking:")
users = dict(sorted(users.items(), key=lambda x: x[0]))
for key, value in users.items():
    print(key)
    value = dict(sorted(value.items(), key=lambda x: -x[1]))
    for k, v in value.items():
        print(f"#  {k} -> {v}")
