import math
num=input().split()
m=int(num[0])
n=int(num[1])
for i in range(m,n+1):
    isit=0
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            isit=1
            break
    if isit==0:
        print(i)