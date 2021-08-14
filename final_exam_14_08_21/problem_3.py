followers = {}
command = input()
while not command == "Log out":
    data = command.split(": ")
    if data[0] == "New follower":
        username = data[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
    elif data[0] == "Like":
        username, count = data[1], int(data[2])
        if username not in followers:
            followers[username] = {'likes': count, 'comments': 0}
        else:
            followers[username]['likes'] += count
    elif data[0] == "Comment":
        username = data[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 1}
        else:
            followers[username]['comments'] += 1
    elif data[0] == "Blocked":
        username = data[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")
    command = input()
result_followers = {key: sum(value.values()) for key, value in followers.items()}
result_followers = dict(sorted(result_followers.items(), key=lambda x: (-x[1], x[0])))
print(f"{len(result_followers)} followers")
for k, v in result_followers.items():
    print(f"{k}: {v}")
