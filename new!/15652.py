def recursion(pos,prev,string):
    global N,M
    if pos==M:
        print(string)
        return
    
    for i in range(1,N+1):
        if prev>i:
            continue
        
        recursion(pos+1,i,string+' '+str(i))
N,M = list(map(int,input().split()))

for i in range(1,N+1):
    recursion(1,i,str(i))
