x=input()
li=x.split()

a=int(li[0])
b=int(li[1])
x=int(li[2])
if a<x:
    x=x-a
    if x%(a-b)==0:
        result=x//(a-b)+1
    else:
        result=x//(a-b)+2

    print(result)
else:
    print(1)