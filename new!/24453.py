import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
error_list = list(map(int,input().split()))
X,Y = list(map(int,input().split()))
error_list.sort()

i1,i2=0,0
min_value = M

while i2<M:
    if i1>=i2 or error_list[i2]-error_list[i1]-1<X:
        i2+=1
    else:
        min_value = min(min_value,i2-i1-1)
        i1+=1
        
while i1<M and N-error_list[i1]>=X:
    min_value = min(min_value,M-i1-1)
    i1+=1
print(M-max(Y,min_value))
