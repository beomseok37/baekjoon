import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))

array = [0 for _ in range(N)]

temp_k = K
temp_n = N-1
cur_num = N
array_i = 0
while temp_k>=temp_n and temp_k>=0 and temp_n >= 0:
    array[array_i] = cur_num
    array_i+=1
    cur_num-=1
    temp_k-=temp_n
    temp_n-=1

if array[N-1-temp_k]==0:
    array[N-1-temp_k] = cur_num
    
temp = 1
for i in range(array_i,N):
    if array[i]==0:
        array[i]=temp
        temp+=1
        
print(' '.join(map(str,array)))
