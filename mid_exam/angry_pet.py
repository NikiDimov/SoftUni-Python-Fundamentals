price_ratings = [int(el) for el in input().split()]
entry_point = int(input())
type_of_items = input()
type_of_price_rating = input()
left_side = price_ratings[:entry_point]
right_side = price_ratings[entry_point + 1:]

if type_of_price_rating == "positive":
    if type_of_items == "cheap":
        sum_left = sum([num for num in left_side if 0 < num < price_ratings[entry_point]])
        sum_right = sum([num for num in right_side if 0 < num < price_ratings[entry_point]])
    else:
        sum_left = sum([num for num in left_side if num > 0 and num >= price_ratings[entry_point]])
        sum_right = sum([num for num in right_side if num > 0 and num >= price_ratings[entry_point]])
elif type_of_price_rating == "negative":
    if type_of_items == "cheap":
        sum_left = sum([num for num in left_side if num < 0 and num < price_ratings[entry_point]])
        sum_right = sum([num for num in right_side if num < 0 and num < price_ratings[entry_point]])
    else:
        sum_left = sum([num for num in left_side if 0 > num >= price_ratings[entry_point]])
        sum_right = sum([num for num in right_side if 0 > num >= price_ratings[entry_point]])
else:
    if type_of_items == "cheap":
        sum_left = sum([num for num in left_side if num < price_ratings[entry_point]])
        sum_right = sum([num for num in right_side if num < price_ratings[entry_point]])
    else:
        sum_left = sum([num for num in left_side if num >= price_ratings[entry_point]])
        sum_right = sum([num for num in right_side if num >= price_ratings[entry_point]])

if sum_left >= sum_right:
    print(f"Left - {sum_left}")
else:
    print(f"Right - {sum_right}")

    

