import sys
input = sys.stdin.readline

N=int(input())
T,P=[],[]
dp=[0 for _ in range(N)]
for i in range(N):
    t,p=list(map(int,input().split()))
    T.append(t)
    P.append(p)

if T[N-1]==1:
    dp[N-1]=P[N-1]
    
for i in range(N-2,-1,-1):
    if i+T[i]-1<N:
        dp[i]=max(dp[i+1],P[i] + (dp[i+T[i]] if i+T[i]<N else 0))
    else:
        dp[i]=dp[i+1]

print(dp[0])
