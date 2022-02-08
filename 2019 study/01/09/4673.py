def d(n):
    result=n
    div=10
    while n>0:
        a=n%div
        result+=a
        n=n//div
    return result

li={}
for i in range(1,10001):
    li[d(i)]=1

for i in range(1,10001):
    if i not in li.keys():
        print(i)