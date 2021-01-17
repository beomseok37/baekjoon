x=int(input())
li=[]
for i in range(x):
    n=input()
    li.append(n.split())

for i in li:
    h=int(i[0])
    w=int(i[1])
    n=int(i[2])
    if n%h==0:
        result=h*100+n//h
    else:
        result=n%h*100+n//h+1
    print(result)