n=int(input())
li=[]
for i in range(n):
    s=input()
    li.append(s)

for i in range(len(li)):
    total=0
    l=li[i].split()
    for s in range(len(l)):
        l[s]=int(l[s])
        if s!=0:
            total+=l[s]
    total=total/l[0]
    num=0
    for j in range(1,l[0]+1):
        if total<l[j]:
            num+=1

    result=num/l[0]*100
    print("%0.3f%%"%result)
