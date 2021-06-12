num = int(input())


def perfect_num_checker(n):
    counter = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            counter += i
    if counter == n:
        return "We have a perfect number!"
    return "It's not so perfect."


print(perfect_num_checker(num))
