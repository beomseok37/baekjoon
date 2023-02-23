import sys
input = sys.stdin.readline

N,K=list(map(int,input().split()))
A=list(map(int,input().split()))

s,e=0,K+1            
while s<e-1:
    x=(s+e)//2
    result = (x*(x+1))//2
    for i in range(N-1):
        difference=A[i+1]-A[i]
        if difference>=x:
            result+=(x*(x+1))//2
        else:
            result+=(2*x-difference+1)*difference//2
    
    if result>=K:
        e=x
    else:
        s=x
print(e)
