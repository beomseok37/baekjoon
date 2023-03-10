import sys
input = sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))

a.sort()
print(a[2*N-1]-a[N])
