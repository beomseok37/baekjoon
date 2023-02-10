import sys
input = sys.stdin.readline

def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

def LCM(x,y):
    return (x*y)//GCD(x,y)

N = int(input())
A = [0]+list(map(int,input().split()))
visited = [False for _ in range(N+1)]
result = 1

for i in range(1,N+1):
    if visited[i]:
        continue
    temp = A[i]
    count = 0
    while True:
        temp = A[temp]
        visited[temp] = True
        count+=1
        
        if temp == A[i]:
            break
        
    result = LCM(result,count)

print(result)
