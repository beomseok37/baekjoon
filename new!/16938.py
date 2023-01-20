import sys
from itertools import combinations
input = sys.stdin.readline

N,L,R,X = list(map(int,input().split()))
difficulty = list(map(int,input().split()))
result=0
difficulty.sort()

for count in range(2,N+1):
    for combination in combinations(difficulty,count):
        if combination[-1] - combination[0] < X or not (L <= sum(combination) <= R):
            continue
        
        result+=1

print(result)
