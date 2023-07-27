import sys
def recursion(pos,result):
    global N,maxAnswer,minAnswer
    
    if pos==N:
        maxAnswer=max(maxAnswer,result)
        minAnswer=min(minAnswer,result)
        return
    
    for i in range(4):
        if calc[i]==0:
            continue

        calc[i]-=1
        if i==0:
            recursion(pos+1,result+A[pos])
        elif i==1:
            recursion(pos+1,result-A[pos])
        elif i==2:
            recursion(pos+1,result*A[pos])
        else:
            if result<0:
                recursion(pos+1,(-1)*(-result//A[pos]))
            else:
                recursion(pos+1,result//A[pos])
        calc[i]+=1
            
N=int(input())
A=list(map(int,input().split()))
calc=list(map(int,input().split()))
minAnswer,maxAnswer=1000000000,-1000000000
recursion(1,A[0])
print(maxAnswer)
print(minAnswer)
