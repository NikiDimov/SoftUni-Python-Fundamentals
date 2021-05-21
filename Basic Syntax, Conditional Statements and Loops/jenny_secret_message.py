def message(name):
    if name == "Johnny":
        return "my love"
    return name


name = input()
print(f"Hello, {message(name)}!")
