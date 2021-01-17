x=input()
li=x.split()
if int(li[1])>=int(li[2]):
    print(-1)
else:
    A=int(li[0])
    B=int(li[1])
    C=int(li[2])
    result = A//(C-B) + 1
    print(result)