row, col=map(int,input().split())
chess=[]
tlist=[]
for i in range(row):
    tmp_str=input()
    tmp_list=[]
    for j in range(col):
        tmp_list.append(tmp_str[j])
    chess.append(tmp_list)

realchesstable1=[]
realchesstable2=[]
black='B'
white='W'
one=1
two=1
for i in range(8):
    tmp1=[]
    tmp2=[]
    for j in range(8):
        if one%2==1:
            if two%2==1:
                tmp1.append(black)
                tmp2.append(white)
            else:
                tmp1.append(white)
                tmp2.append(black)
        else:
            if two%2==1:
                tmp2.append(black)
                tmp1.append(white)
            else:
                tmp2.append(white)
                tmp1.append(black)
        two+=1
    one+=1
    realchesstable1.append(tmp1)
    realchesstable2.append(tmp2)
    
def findDifferent(r,c):
    check1=0
    check2=0
    for i in range(8):
        for j in range(8):
            if chess[r+i][c+j]!=realchesstable1[i][j]:
                check1+=1
            if chess[r+i][c+j]!=realchesstable2[i][j]:
                check2+=1
    if check1<check2:
        return check1
    else:
        return check2

min=findDifferent(0,0)
for r in range(row-7):
    for c in range(col-7):
        compare=findDifferent(r,c)
        if min>compare:
            min=compare
        
print(min)