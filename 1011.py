# num=int(input())
# li=[]
# for i in range(num):
#     s=input()
#     l=s.split()
#     li.append(int(l[1])-int(l[0]))
# c=[]
# for i in range(num):
#     l=[]
#     for i in range(li[i]+1):
#         l.append(0)
#     c.append(l)
# def func(n,x,k,y):
#     if x==n:
#         if k==1:
#             c[y][x-1]=0
#             return 0
#         else:
#             return 1000000000
#     elif n<x+(k-1)*(k-2)/2:
#         return 1000000000
#     elif x>n:
#         return 1000000000
#     else:
#         if k==0:
#             result=func(n,x+1,1,y)+1
#         elif k==1:
#             if c[y][x+k-1]==0:
#                 a=func(n,x+k,k,y)
#                 c[y][x+k-1]=a
#             else:
#                 a=c[y][x+k-1]
#             if c[y][x+k]==0:
#                 b=func(n,x+k+1,k+1,y)
#                 c[y][x+k]=b
#             else:
#                 b=c[y][x+k]
#             result=min(a,b)+1
#         else:
#             if c[y][x+k-2]==0:
#                 a=func(n,x+k-1,k-1,y)
#                 c[y][x+k-2]=a
#             else:
#                 a=c[y][x+k-2]
#             if c[y][x+k-1]==0:
#                 b=func(n,x+k,k,y)
#                 c[y][x+k-1]=b
#             else:
#                 b=c[y][x+k-1]
#             if c[y][x+k]==0:
#                 d=func(n,x+k+1,k+1,y)
#                 c[y][x+k]=d
#             else:
#                 d=c[y][x+k]
#             result=min(a,b,d)+1
#         c[y][x-1]=result
#         return result

# for i in range(num):
#     print(func(li[i],0,0,i))

num=int(input())
li=[]
for i in range(num):
    s=input()
    l=s.split()
    li.append(int(l[1])-int(l[0]))

for i in range(num):
    move=0
    count=0
    nowmove=1
    while li[i]>move:
        move+=nowmove
        count+=1
        if count%2==0:
            nowmove+=1
    print(count)