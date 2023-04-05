import math
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B,C=list(map(int,input().split()))
result=0

for room in A:
    temp = 0 if room-B<0 else room-B
    result+=1 + math.ceil((temp)/C)

print(result)
