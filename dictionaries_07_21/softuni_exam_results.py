command = input()
results = {}
submissions = {}


def result(dict_info):
    dict_info = dict(sorted(dict_info.items(), key=lambda x: x[0]))
    dict_info = dict(sorted(dict_info.items(), key=lambda x: -x[1]))
    return dict_info


while not command == "exam finished":
    data = command.split('-')
    if not data[1] == "banned":
        username, language, points = data[0], data[1], int(data[2])
        if username not in results:
            results[username] = [points]
        else:
            results[username].append(points)
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        username = data[0]
        if username in results:
            del results[username]
    command = input()

results = {k: max(v) for k, v in results.items()}

print("Results:")
for k, v in result(results).items():
    print(f"{k} | {v}")
print("Submissions:")
for k, v in result(submissions).items():
    print(f"{k} - {v}")
