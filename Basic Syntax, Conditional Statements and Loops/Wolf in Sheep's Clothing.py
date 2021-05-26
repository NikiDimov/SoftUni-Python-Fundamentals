herd = input().split(", ")
if herd[-1] == "wolf":
    print(f"Please go away and stop eating my sheep")
else:
    herd = herd[::-1]
    print(f"Oi! Sheep number {herd.index('wolf')}! You are about to be eaten by a wolf!")
