from itertools import combinations
N=int(input())
equation=list(input())
max_value=int(equation[0])
for i in range(1,N,2):
    if equation[i]=='+':
        max_value+=int(equation[i+1])
    elif equation[i]=='-':
        max_value-=int(equation[i+1])
    else:
        max_value*=int(equation[i+1])

for i in range(1,(N//2)):
    for combs in combinations(range(1,N,2),i):
        for c in range(len(combs)-1):
            if abs(combs[c]-combs[c+1])==2:
                break
        else:
            j,k=0,0
            temp=[]
            while k<N:
                if j<i and combs[j]==k:
                    temp.pop()
                    if equation[k]=='+':
                        temp.append(int(equation[k-1])+int(equation[k+1]))
                    elif equation[k]=='-':
                        temp.append(int(equation[k-1])-int(equation[k+1]))
                    else:
                        temp.append(int(equation[k-1])*int(equation[k+1]))
                    j+=1
                    k+=1
                else:
                    temp.append(equation[k])
                k+=1
            
            value=int(temp[0])
            for j in range(1,len(temp),2):
                if temp[j]=='+':
                    value+=int(temp[j+1])
                elif temp[j]=='-':
                    value-=int(temp[j+1])
                else:
                    value*=int(temp[j+1])
            max_value=max(max_value,value)
print(max_value)
