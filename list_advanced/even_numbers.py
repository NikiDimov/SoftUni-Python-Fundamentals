single_string = input().split(", ")
new_list = list(map(lambda x: int(x), single_string))
even_numbers = [index for index in range(len(new_list)) if new_list[index] % 2 == 0]
print(even_numbers)
