n=int(input())
s=input()
l=s.split()
li=[]
for i in range(n):
    li.append(int(l[i]))
li.sort()
total=0
for i in range(n):
    total+=li[i]/li[-1]*100
print(total/n)