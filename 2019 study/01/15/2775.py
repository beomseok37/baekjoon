num=int(input())
kl=[]
nl=[]
for i in range(num):
    x=int(input())
    y=int(input())
    kl.append(x)
    nl.append(y)

for i in range(num):
    k=kl[i]
    n=nl[i]
    li=[]
    for j in range(n):
        li.append(j+1)
    for j in range(n,(k+1)*n):
        li.append(0)
    def func(a,b):
        result=0
        for d in range(1,b+1):
            if li[(a-1)*n+d-1]==0:
                result+=func(a-1,d)
            else:
                result+=li[(a-1)*n+d-1]
        if li[a*n+b-1]==0:
            li[a*n+b-1]=result
        return li[a*n+b-1]
    
    print(func(k,n))