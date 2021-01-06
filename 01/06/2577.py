num=[]
for i in range(3):
    n=int(input())
    num.append(n)

result=str(num[0]*num[1]*num[2])
for i in range(10):
    n=0
    for s in result:
        if s==str(i):
            n=n+1
    print(n)