import sys
input = sys.stdin.readline

N,X=list(map(int,input().split()))
taste_list=[list(map(int,input().split())) for i in range(N)]
sorted_taste=sorted(taste_list,key=lambda x:x[0]-x[1],reverse=True)

X-=1000*N
result=sum([taste[1] for taste in sorted_taste])
for taste in sorted_taste:
    if X>=4000 and taste[0]>taste[1]:
        X-=4000
        result+=taste[0]-taste[1]
    else:
        break
print(result)
