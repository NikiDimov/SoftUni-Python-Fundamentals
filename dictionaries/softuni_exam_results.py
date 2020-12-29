command = input()
results = {}
submissions = {}

while not command == "exam finished":
    text = command.split("-")
    if len(text) == 3:
        user_name = text[0]
        language = text[1]
        points = int(text[2])
        if user_name not in results:
            results[user_name] = []
        results[user_name].append(points)
        if language not in submissions:
            submissions[language] = []
        submissions[language].append(points)

    elif len(text) == 2:
        user_name = text[0]
        results.pop(user_name)

    command = input()

for key, max_result in results.items():
    results[key] = max(max_result)
for key, count in submissions.items():
    submissions[key] = len(count)

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for key, value in results.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
