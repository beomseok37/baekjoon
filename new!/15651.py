def recursion(pos,string):
    global N,M
    if M==pos:
        print(string)
        return
        
    for i in range(1,N+1):
        recursion(pos+1,string+' '+str(i))

N,M=list(map(int,input().split()))

for i in range(1,N+1):
    recursion(1,str(i))
