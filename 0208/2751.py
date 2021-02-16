# number=int(input())

# numblist=[]
# for i in range(number):
#     x=int(input())
#     numblist.append(x)

# sorted=[0]*len(numblist)
# def merge(left,mid,right):
#     i=left
#     j=mid+1
#     k=left

#     while i<=mid and j<=right:
#         if numblist[i]<numblist[j]:
#             sorted[k]=numblist[i]
#             i+=1
#         else:
#             sorted[k]=numblist[j]
#             j+=1
#         k+=1
#     if i<=mid:
#         for a in range(i,mid+1):
#             sorted[k]=numblist[a]
#             k+=1
#     else:
#         for a in range(j,right+1):
#             sorted[k]=numblist[a]
#             k+=1
#     for a in range(left,right+1):
#         numblist[a]=sorted[a]

# def mergesort(left,right):
#     if left<right:
#         mid=(left+right)//2
#         mergesort(left,mid)
#         mergesort(mid+1,right)
#         merge(left,mid,right)

# mergesort(0,len(numblist)-1)
# for i in numblist:
#     print(i)

import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')