s=input()
li=s.split()
l1=[]
l2=[]
for i in range(3):
    l1.append(li[0][2-i])
    l2.append(li[1][2-i])

for i in range(3):
    if l1[i]>l2[i]:
        for s in range(3):
            print(l1[s],end="")
        break
    elif l1[i]<l2[i]:
        for s in range(3):
            print(l2[s],end="")
        break
    else:
        continue