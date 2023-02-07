import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int,input().split()))

result = 2*H[0]**2 + 2*H[N-1]**2
for i in range(1,N-1):
    result+= 4*H[i]**2

print(result)
