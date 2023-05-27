import sys
input = sys.stdin.readline

T=int(input())
for t in range(T):
    k=int(input())
    files=list(map(int,input().split()))
    
    dp=[[0 for _ in range(k)] for __ in range(k)]
    prefix=[files[0] for _ in range(k)]
    for i in range(1,k):
        prefix[i]=prefix[i-1]+files[i]
    
    for i in range(1,k):
        for j in range(k-1):
            if i+j>=k:
                break
            
            temp=sys.maxsize
            total=prefix[j+i]-(prefix[j-1] if j>=1 else 0)
            for l in range(j,j+i):
                temp=min(temp,dp[j][l]+dp[l+1][j+i]+total)
            dp[j][j+i]=temp
    
    print(dp[0][k-1])
