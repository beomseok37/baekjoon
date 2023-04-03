import sys
input = sys.stdin.readline

T=int(input())
test_case_list=[]
for i in range(T):
    test_case_list.append([int(input()),list(map(int,input().split()))])

for n,L in test_case_list:
    L.sort(reverse=True)
    result=0
    
    prev=L[0]
    for i in range(2,n,2):
        result=max(result,prev-L[i])
        prev=L[i]
    
    prev=L[0]
    for i in range(1,n,2):
        result=max(result,prev-L[i])
        prev=L[i]
    print(result)
