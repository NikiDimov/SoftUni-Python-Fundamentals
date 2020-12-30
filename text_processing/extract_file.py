path_to_a_file = input().split("\\")
file = path_to_a_file[-1]
file_name, file_extension = file.split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
