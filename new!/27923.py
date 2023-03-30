import sys
input = sys.stdin.readline

N,K,L=list(map(int,input().split()))
m=list(map(int,input().split()))
t=sorted(list(map(int,input().split())))
drink=[0 for _ in range(N)]
prefix_drink=[0 for _ in range(N)]
result=0

for time in t:
    drink[time-1]+=1

count=0
array=[]
for i in range(N):
    if drink[i]!=0:
        array.append(i)
        count+=drink[i]
    
    if array and i-array[0]>=L:
        count-=drink[array.pop(0)]
        
        
    prefix_drink[i]+=count

prefix_drink.sort()
m.sort()

for i,c in enumerate(prefix_drink):
    result += m[i]//(2**c)
    
print(result)
