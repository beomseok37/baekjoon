def recursion(n):
    if dp[n]!=0:
        return dp[n]
    
    dp[n]=recursion(n-1)+recursion(n-5)
    return dp[n]

T=int(input())
tList=[int(input()) for _ in range(T)]
dp=[0 for _ in range(max(tList))]
dp[0]=1
dp[1]=1
dp[2]=1
dp[3]=2
dp[4]=2

for t in tList:
    print(recursion(t-1))
