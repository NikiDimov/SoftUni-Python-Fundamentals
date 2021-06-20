n = int(input())
shells = []
counter = 0
while True:
    counter += 1
    current_shell = 2 * counter ** 2
    if sum(shells) == n:
        break
    elif sum(shells) + current_shell > n:
        shells.append(n-sum(shells))
        break
    else:
        shells.append(current_shell)
print(shells)
