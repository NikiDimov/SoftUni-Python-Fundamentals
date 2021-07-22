line = input()
power = 0
a = len(line)
try:
    for i in range(len(line)):
        if line[i] == ">":
            power += int(line[i + 1])
            while power > 0:
                if line[i+1] == ">":
                    break
                line = line[:i+1]+line[i+2:]
                power -= 1
except(BaseException):
    print(line)
    