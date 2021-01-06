l={}
j=[]
for i in range(9):
    num=int(input())
    l[num]=i
    j.append(num)

j.sort()
print(j[-1])
print(l[j[-1]]+1)