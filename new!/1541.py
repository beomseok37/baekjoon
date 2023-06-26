string=input()

temp=0
equation=[]
for s in string:
    if s=='-' or s=='+':
        equation.append(temp)
        equation.append(s)
        temp=0
    else:
        temp*=10
        temp+=int(s)
equation.append(temp)

flag=False
result=0
for e in equation:
    if e=='-':
        flag=True
    
    if e=='-' or e=='+':
        continue
    
    result += -e if flag else e

print(result)
