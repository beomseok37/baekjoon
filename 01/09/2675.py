num=int(input())
li=[]
for i in range(num):
    s=input()
    li.append(s.split())

for i in li:
    n=int(i[0])
    for j in i[1]:
        for k in range(n):
            print(j,end="")
    print()