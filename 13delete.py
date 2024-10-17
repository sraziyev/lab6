import os

file_path = input()

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"Access denied. You do not have permission to delete '{file_path}'.")
else:
    print(f"File '{file_path}' does not exist.")
