def find(a):
    if len(a)==4:
        return 0
    dif=a[0]-a[1]
    if dif == a[1]-a[2]:
        return 1
    else:
        return 0

def isit(n):
    a=[]
    while n>0:
        a.append(n%10)
        n=n//10
    result=find(a)
    return result

num=int(input())
total=0
for i in range(1,num+1):
    if i>=100:
        if isit(i)==1:
            total+=1
    else:
        total+=1
print(total)