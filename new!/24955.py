from collections import defaultdict
import sys
input = sys.stdin.readline

def find(start,end):
    visited=[False for _ in range(N+1)]
    now = start
    result=''
    
    stack = [[A[now],now]]
    visited[now] = True
    while True:
        result,now = stack.pop()
        
        if now==end:
            break
        
        for next_house in roads[now]:
            if not visited[next_house]:
                visited[next_house]=True
                next_result = result+A[next_house]
                stack.append([next_result,next_house])

    return result

N,Q =list(map(int,input().split()))
A=[0]+list(input().split())
roads=defaultdict(list)
questions = []

for i in range(N-1):
    ai,bi=list(map(int,input().split()))
    roads[ai].append(bi)
    roads[bi].append(ai)

for i in range(Q):
    questions.append(list(map(int,input().split())))

for xi,yi in questions:
    print(int(find(xi,yi))%1000000007)
