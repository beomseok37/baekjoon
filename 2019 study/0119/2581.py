m=int(input())
n=int(input())
result=[]
for check in range(m,n+1):
    isit=0
    if check==1:
        isit=1
    else:
        for j in range(2,check):
            if check%j==0:
                isit=1
                break
    if isit==0:
        result.append(check)
sum=0
for i in result:
    sum+=i
if len(result)>0:
    print(sum)
    print(result[0])
else:
    print(-1)