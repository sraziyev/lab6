path = input()
with open(path, 'r') as file:
    lines = file.readlines()
print(f"The file contains {len(lines)} lines.")
