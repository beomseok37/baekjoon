num=int(input())
Quiz=[]


for i in range(num):
    n=input()
    Quiz.append(n)

for i in range(num):
    num=0
    result=0
    for j in range(len(Quiz[i])):
        if Quiz[i][j]=='O':
            num=num+1
        else:
            num=0
        result=result+num
    print(result)