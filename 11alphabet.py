import os
import string

directory = input()
if not os.path.exists(directory):
    os.makedirs(directory)
for letter in string.ascii_uppercase:
    filename = os.path.join(directory, f"{letter}.txt")
print("Finished")
