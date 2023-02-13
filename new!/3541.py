import sys
input = sys.stdin.readline

def GCD(x,y):
    while y:
        x,y=y,x%y
    return x

def LCM(x,y):
    return (x*y)//GCD(x,y)

n,m = list(map(int,input().split()))
u,d=[],[]
result = sys.maxsize

for i in range(m):
    ui,di = list(map(int,input().split()))
    u.append(ui)
    d.append(di)
    
for i in range(m):
    ui,di = u[i],d[i]
    lcm = LCM(ui,di)
    remain = n % (lcm//ui+lcm//di)

    count = 0
    total = 0
    while remain>count:
        count+=1
        if total - di>0:
            total-=di
        else:
            total+=ui
    
    if total==0:
        total = ui+di
    
    result = min(total,result)
print(result)
