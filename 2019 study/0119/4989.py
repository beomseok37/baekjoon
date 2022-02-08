n=123456*2+1
rlist=[True]*n
for i in range(2,n):
    if rlist[i]:
        for j in range(i*2,n,i):
            rlist[j]=False

ilist=[]
while 1:
    x=int(input())
    if x==0:
        break
    ilist.append(x)

for i in ilist:
    count=0
    for j in range(i+1,2*i+1):
        if rlist[j]:
            count+=1
    print(count)