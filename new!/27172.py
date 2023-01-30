import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))
result = [-1 for _ in range(1000001)]

for i in range(N):
    result[array[i]]=0

sorted_array = sorted(array)

for i in range(N-1):
    for j in range(2,(sorted_array[-1]//sorted_array[i])+1):
        if result[sorted_array[i]*j]>=0:
            result[sorted_array[i]*j]+=1
            result[sorted_array[i]]-=1
            
for i in range(N):
    print((-1)*result[array[i]],end=" " if i !=N-1 else "\n")
