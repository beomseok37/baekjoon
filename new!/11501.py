import sys
input = sys.stdin.readline

def find_max_index(trade_list):
    index = 0
    for i in range(1,len(trade_list)):
        if trade_list[index]<=trade_list[i]:
            index=i
    return index

T = int(input())
t = []
for _ in range(T):
    t.append([])
    t[-1].append(int(input()))
    t[-1].append(list(map(int,input().split())))

for N,trade_list in t:
    result = 0
    index = 0
    while index<N:
        max_index = find_max_index(trade_list[index:])

        if max_index==0:
            index+=1
            continue
        
        for i in range(index,index+max_index):
            result+=trade_list[index+max_index]-trade_list[i]
        
        index = index+max_index+1
    print(result)
