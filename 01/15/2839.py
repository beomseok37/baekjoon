# num=int(input())
# li=[]
# for i in range(num+1):
#     li.append(0)
# def func(n):
#     if n==0:
#         return 0
#     if n-5<0:
#         a=10000
#     elif li[n-5]==0:
#         a=func(n-5)+1
#     else:
#         a=li[n-5]+1
#     if n-3<0:
#         b=10000
#     elif li[n-3]==0:
#         b=func(n-3)+1
#     else:
#         b=li[n-3]+1
#     li[n]=min(a,b)
#     return li[n]
# result=func(num)
# if result>=10000:
#     print(-1)
# else:
#     print(func(num))

num=int(input())
isit=1
result=0
if num%5==0:
    result=num//5
    isit=0
else:
    for i in range(num//5,-1,-1):
        x=num-i*5
        if x%3==0:
            result=i+x//3
            isit=0
            break
if isit==0:
    print(result)
else:
    print(-1)