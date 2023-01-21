from __future__ import print_function
from functools import cmp_to_key
import sys
input = sys.stdin.readline

def compare(x,y):
    if x[1]!=y[1]:
        return y[1]-x[1]
    else:
        return y[0]-x[0]
    
H,N = list(map(int,input().split()))
info = []
dp = [False for _ in range(H+1)]
dp[0] = True
result = 0

for _ in range(N):
    info.append(list(map(int,input().split())))
info.sort(key=cmp_to_key(compare))

for i in range(N):
    if dp[H-info[i][0]]:
        result = info[i][1]
        break
    
    new_dp = dp[:]
    new_dp[0] = True
    for j in range(H+1-info[i][0]):
        if dp[j]:
            new_dp[j+info[i][0]] = True
    dp=new_dp[:]
print(result)
