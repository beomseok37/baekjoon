N=int(input())
array=[[int(input())]]
for i in range(N-1):
    array.append(list(map(int,input().split())))

dp=array[:]
for i in range(1,N):
    for j in range(i+1):
        x,y=j-1,j
        
        if j==0:
            dp[i][j]=dp[i][j]+dp[i-1][j]
        elif 1<=j<i:
            dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i-1][j])
        else:
            dp[i][j]=dp[i][j]+dp[i-1][j-1]
print(max(dp[N-1]))
