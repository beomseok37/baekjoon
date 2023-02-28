import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
max_A=[0]
max_B=[0]
for i in range(1,N):
    if A[max_A[0]]<A[i]:
        max_A=[i]
    elif A[max_A[0]]==A[i]:
        max_A.append(i)
for i in range(1,M):
    if B[max_B[0]]<B[i]:
        max_B=[i]
    elif B[max_B[0]]==B[i]:
        max_B.append(i)

answer=0
for i in range(max_A[0]):
    answer+=A[i]*10**9+B[0]

if len(max_A)==1:
    for i in range(M-1):
        answer+=A[max_A[0]]*10**9+B[i]
    for i in range(max_A[0],N):
        answer+=A[i]*10**9+B[M-1]
else:
    for i in range(max_B[0]):
        answer+=A[max_A[0]]*10**9+B[i]
    for i in range(max_A[0],max_A[-1]):
        answer+=A[i]*10**9+B[max_B[0]]
    for i in range(max_B[0],M-1):
        answer+=A[max_A[-1]]*10**9+B[i]
    for i in range(max_A[-1],N):
        answer+=A[i]*10**9+B[M-1]
        
print(answer)
