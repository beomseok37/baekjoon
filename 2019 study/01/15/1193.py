num=int(input())*2

n=0
while n*(n+1) < num:
    n+=1
if n%2==0:
    front=(num-(n-1)*n)//2
    back=n-front+1
else:
    back=(num-(n-1)*n)//2
    front=n-back+1
print(str(front)+"/"+str(back))