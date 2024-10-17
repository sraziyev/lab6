my_list = []
print("Enter items for the list (type 'finish' to finish):")
while True:
    item = input("> ")
    if item.lower() == 'finish':
        break
    my_list.append(item)

with open("list.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

print("Finished")
