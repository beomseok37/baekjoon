import sys
input = sys.stdin.readline

def change_input(number):
    global i
    i+=1
    return [i,int(number)]

N,K = list(map(int,input().split()))
i=0
c = list(map(change_input,input().split()))
result = [0 for _ in range(N)]

c.sort(key=lambda x: x[1],reverse=True)

ci,ri=0,0
while ci<K:
    j=0
    while j<c[ci][1]:
        result[ri]=c[ci][0]
        ri+=2
        j+=1
        if ri>N-1:
            ri=1
    ci+=1

if N>1 and result[0]==result[1]:
    print(-1)
else:
    print(' '.join(map(str,result)))
