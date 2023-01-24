import sys
input = sys.stdin.readline

def func(x,y,a):
    b = (x**2-a**2)**0.5
    d = (y**2-a**2)**0.5
    c = b*d/(b+d)
    return c

x,y,c = list(map(float,input().split()))
start,end = 0, min(x,y)
result = 0

while end-start>0.000001:
    middle = (end+start)/2
    if func(x,y,middle)>=c:
        result=middle
        start=middle
    else:
        end = middle

print(result)
