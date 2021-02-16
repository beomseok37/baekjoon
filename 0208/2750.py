number=int(input())

numblist=[]
for i in range(number):
    x=int(input())
    numblist.append(x)

numblist.sort()
for i in numblist:
    print(i)