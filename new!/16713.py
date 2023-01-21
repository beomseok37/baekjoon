import sys
input = sys.stdin.readline

def xor(num_list):
    result = num_list[0]
    for i in range(1,len(num_list)):
        result = result^num_list[i]
    return result

N,Q = list(map(int,input().split()))
a = list(map(int,input().split()))
prefix_a = [0]
s_e = []
result = []

for _ in range(Q):
    s_e.append(list(map(int,input().split())))

prefix_a.append(a[0])
for i in range(1,N):
    prefix_a.append(prefix_a[-1]^a[i])

for s,e in s_e:
    result.append(prefix_a[e]^prefix_a[s-1])
        
print(xor(result))
