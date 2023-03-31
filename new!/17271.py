import sys
input = sys.stdin.readline

N,m=list(map(int,input().split()))
dp=[0 for _ in range(10001)]
result=0

i,temp=0,1
while i<=N:
    dp[i]=temp
    i+=1
    temp*=i

for b in range(N//m+1):
    a=N-m*b
    result+=dp[a+b]//(dp[a]*dp[b])

print(result%1000000007)
