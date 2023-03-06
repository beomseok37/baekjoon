import sys
input = sys.stdin.readline

def solution(index,count):
    global n
    if dp[index][count]!=-1:
        return dp[index][count]
    
    return_value=1
    
    for i in range(index+1,n):
        if a[index]>a[i] and count>0:
            return_value=max(return_value,solution(i,count-1)+1)
        if a[index]<=a[i]:
            return_value=max(return_value,solution(i,count)+1)
    
    dp[index][count]=return_value
    return return_value

n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
dp=[[-1 for _ in range(501)] for __ in range(501)]

print(solution(0,k))
