import sys
input = sys.stdin.readline

n,m,t=list(map(int,input().split()))
n,m=min(n,m),max(n,m)
length = t//n+1
burger = [[0 for i in range(length)],[0 for i in range(length)],[0 for i in range(length)]]
coke_min = sys.maxsize
result=0

for i in range(length):
    burger[0][i]=i*n
    burger[1][i]=((t-i*n)//m)*m
    burger[2][i]=t-burger[0][i]-burger[1][i]
    if burger[2][i]<coke_min:
        result=i+(t-i*n)//m
        coke_min=burger[2][i]
    elif burger[2][i]==coke_min:
        result=max(result,i+(t-i*n)//m)
print(str(result)+' '+str(coke_min))
