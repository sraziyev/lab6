text=input()
u=0
l=0
for x in text:
    if x.isupper():
        u=u+1
    else:
        l=l+1
print("Uppercase letters: ",u,"Lowercase letters: ",l )