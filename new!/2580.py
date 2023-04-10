import sys
input = sys.stdin.readline

def check_row(r,num):
    for i in range(9):
        if num==sudoku[r][i]:
            return False
    return True

def check_column(c,num):
    for i in range(9):
        if num==sudoku[i][c]:
            return False
    return True

def check_box(r,c,num):
    x=(r//3)*3
    y=(c//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[x+i][y+j]==num:
                return False
    return True

def recursion(count):
    if count==len(zeros):
        for i in range(9):
            print(' '.join(map(str,sudoku[i])))
        exit()
    
    r,c=zeros[count]
    
    for num in range(1,10):
        if check_row(r,num) and check_column(c,num) and check_box(r,c,num):
            sudoku[r][c]=num
            recursion(count+1)
            sudoku[r][c]=0


sudoku=[list(map(int,input().split())) for _ in range(9)]
zeros=[]
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zeros.append([i,j])
recursion(0)

