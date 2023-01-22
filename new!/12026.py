import sys
input = sys.stdin.readline

N = int(input())
BOJ = list(input())[:-1]
dp = [sys.maxsize for _ in range(N)]
dp[0]=0

for i in range(0,N-1):
    for j in range(i+1,N):
        if BOJ[i]=='B' and BOJ[j]=='O':
            dp[j] = min(dp[j],dp[i]+(j-i)**2)
        elif BOJ[i]=='O' and BOJ[j]=='J':
            dp[j] = min(dp[j],dp[i]+(j-i)**2)
        elif BOJ[i]=='J' and BOJ[j]=='B':
            dp[j] = min(dp[j],dp[i]+(j-i)**2)

print(dp[-1] if dp[-1]!=sys.maxsize else -1)
