'''a=tuple(input().split())
answer=True
for x in a:
    if not x:
        answer=False
        break

if answer:
    print("All inputs are True")
else: 
    print("False")'''


a=tuple(input().split(' '))
if all(a) and all(i!='0' for i in a) and all(i!=False for i in a):
    print("True")
else:
    print("False")