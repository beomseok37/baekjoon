import sys
input = sys.stdin.readline

N = int(input())
s,e=[],[]
result=[]
life_span = 0
for i in range(N):
    si,ei=list(map(int,input().split()))
    s.append(si)
    e.append(ei)
    
start,end=s[0],e[0]
index = 1
while index<N:
    if s[index]>end:
        result = [end for _ in range(index)]
        break
    elif e[index]<start:
        result = [start for _ in range(index)]
        break
    elif start<=s[index] and e[index]<=end:
        start=s[index]
        end=e[index]
    elif start<=s[index]<=end and e[index]>end:
        start=s[index]
    elif start<=e[index]<=end and s[index]<start:
        end=e[index]
    
    index+=1
    
if index==N:
    result = [start for _ in range(N)]

for i in range(index,N):
    if s[i]<=result[-1]<=e[i]:
        result.append(result[-1])
    elif result[-1]<s[i]:
        life_span+=s[i]-result[-1]
        result.append(s[i])
    else:
        life_span+=result[-1]-e[i]
        result.append(e[i])

print(life_span)
for i in range(N):
    print(result[i])
