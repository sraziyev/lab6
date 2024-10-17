import os

path = input()


if not os.path.exists(path):
    print(f"The specified path '{path}' does not exist.")
else:
    print(f"The specified path '{path}' exists.")
    if os.access(path, os.R_OK):
        print(f"The path '{path}' is readable.")
    else:
        print(f"The path '{path}' is not readable.")
    if os.access(path, os.W_OK):
        print(f"The path '{path}' is writable.")
    else:
        print(f"The path '{path}' is not writable.")
    if os.access(path, os.X_OK):
        print(f"The path '{path}' is executable.")
    else:
        print(f"The path '{path}' is not executable.")