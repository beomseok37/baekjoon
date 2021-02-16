number=input()

numblist=[]
for i in number:
    numblist.append(int(i))

numblist.sort(reverse=True)
for i in numblist:
    print(i,end="")