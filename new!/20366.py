import sys
input = sys.stdin.readline

N=int(input())
H=list(map(int,input().split()))
H.sort()
minimum=sys.maxsize

for i in range(N):
    for j in range(i+3,N):
        s,e=i+1,j-1
        while s<e:
            temp=H[i]+H[j]-H[s]-H[e]
            if minimum>abs(temp):
                minimum=abs(temp)
                
            if temp<0:
                e-=1
            else:
                s+=1
    
print(minimum)
