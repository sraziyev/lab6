word=input()
d=len(word)
a=int(d/2)
f=0
l=d-1
answer=True
while f<a:
    if word[f]!=word[l]:
        answer=False
        break
    f+=1
    l=l-1
if answer:
    print("The word ",word,"is palindrome")
else:
    print("The word",word,"isn't palindrome")
