from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def get_point_distance(x, y):
    return abs(x) + abs(y)


first_point_distance = get_point_distance(x1, y1)
second_point_distance = get_point_distance(x2, y2)

if first_point_distance <= second_point_distance:
    print((floor(x1), floor(y1)))
else:
    print((floor(x2), floor(y2)))

