source_file = input("From which file to copy from?")
destination_file = input("To which file input the data?")
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line)
print(f"Contents of {source_file} have been copied to {destination_file}.")
