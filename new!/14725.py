N=int(input())
ant=[]
for i in range(N):
    count,*info = input().split()
    ant.append(info)

ant.sort(key=lambda x:''.join(x))
ant = list(map(list,ant))

for i in range(len(ant[0])):
    print('--'*i+ant[0][i])

for i in range(1,N):
    j=0
    while j<min(len(ant[i-1]),len(ant[i])):
        if ant[i-1][j]!=ant[i][j]:
            break
        j+=1
    for k in range(j,len(ant[i])):
        print('--'*k+ant[i][k])
