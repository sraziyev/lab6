import os

path = input()

if os.path.exists(path):
    print(f"The path '{path}' exists.")
    filename = os.path.basename(path)
    print(f"Filename portion: {filename}")
    directory = os.path.dirname(path)
    print(f"Directory portion: {directory}")
else:
    print(f"The path '{path}' does not exist.")