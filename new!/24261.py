import sys
input = sys.stdin.readline

def solution(small,big,flag):
    global n,m
    
    if flag:
        n,m=m,n
        
    temp={}
    j=0
    for i in range(n+1):
        while j<m and small[i]>big[j+1]:
            j+=1
        t=small[i]-big[j]
        if t not in temp:
            temp[t]=[]
            temp[t].append([i,j])
        else:
            prev_i,prev_j=temp[t].pop()
            if flag:
                print_solution(prev_j,j)
                print_solution(prev_i,i)
            else:
                print_solution(prev_i,i)
                print_solution(prev_j,j)
            exit()

def print_solution(prev,curr):
    print(curr-prev)
    print(' '.join(map(str,[number for number in range(prev,curr)])))

n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

pre_A,pre_B=[0],[0]
for a in A:
    pre_A.append(pre_A[-1]+a)
for b in B:
    pre_B.append(pre_B[-1]+b)

if pre_A[-1]<=pre_B[-1]:
    solution(pre_A,pre_B,False)
else:
    solution(pre_B,pre_A,True)
