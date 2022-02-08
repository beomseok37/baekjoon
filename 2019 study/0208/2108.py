import sys
from collections import Counter
number=int(sys.stdin.readline())

numblist=[]
numbdic={}
for i in range(number):
    x=int(sys.stdin.readline())
    numblist.append(x)

numblist.sort()
total=0
for i in numblist:
    total+=i

one=round(total/len(numblist))
if len(numblist)%2==1:
    two=numblist[len(numblist)//2]
else:
    two=(numblist[len(numblist)//2-1]+numblist[len(numblist)//2])

numbdic=Counter(numblist).most_common()
four=numblist[-1]-numblist[0]
print(one)
print(two)
if len(numblist)==1:
    print(numbdic[0][0])
else:
    if numbdic[0][1]==numbdic[1][1]:
        print(numbdic[1][0])
    else:
        print(numbdic[0][0])
print(four)