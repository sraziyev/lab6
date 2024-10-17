import os

path = input()
print("Only directories:")
directories = [dir_name for dir_name in os.listdir(path) if os.path.isdir(os.path.join(path, dir_name))]
for directory in directories:
    print(directory)

print("\nFiles:")
files = [file_name for file_name in os.listdir(path) if os.path.isfile(os.path.join(path, file_name))]
for file in files:
    print(file)

print("\nFiles and all directories:")
for both in os.listdir(path):
    print(both)