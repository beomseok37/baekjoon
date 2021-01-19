n=10001
rlist=[True]*n
for i in range(2,n):
    if rlist[i]:
        for j in range(i*2,n,i):
            rlist[j]=False

num=int(input())
nlist=[]
for i in range(num):
    x=int(input())
    nlist.append(x)

for i in nlist:
    minlist=[]
    for j in range(2,i//2+1):
        if rlist[j] and rlist[i-j]:
            minlist.append([j,i-j])
    print(str(minlist[-1][0])+" "+str(str(minlist[-1][1])))