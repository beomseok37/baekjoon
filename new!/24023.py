import sys
input = sys.stdin.readline

N,K= list(map(int,input().split()))
A = [0]+list(map(int,input().split()))
binary = [[] for __ in range(N+1)]
pointer = [0 for _ in range(30)]
pointer_result = A[1]

for i in range(1,N+1):
    temp_a = A[i]
    new_binary = ''
    while temp_a!=0:
        new_binary += str(temp_a%2)
        temp_a= temp_a//2
        
    for bi,b in enumerate(list(map(int,new_binary))):
        if b==1:
            binary[i].append(bi)

s,e = 1,1
for i in binary[1]:
    pointer[i]=1

while s<=e and pointer_result!=K:
    if e<N and (s==e or pointer_result<K):
        e+=1
        for i in binary[e]:
            pointer[i]+=1
        pointer_result=pointer_result|A[e]
    else:
        for i in binary[s]:
            pointer[i]-=1
            if pointer[i]<1:
                pointer_result-=2**i
        s+=1
    
if pointer_result==K:
    print(str(s)+" "+str(e))
else:
    print(-1)
