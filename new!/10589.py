import sys
input = sys.stdin.readline

def is_even(num):
    return num%2==0

def count(num):
    if num==1:
        return 0
    
    if num%2==0:
        return ((num//2)//2)*2 if (num//2)%2==1 else ((num//2)//2)*2-1
    else:
        return num//2
        
def N_even_func(num,opposite_num):
    if num<=2:
        return
    if (num//2)%2==1:
        for n in range(2,num//2+1,2):
            print(n,1,n,opposite_num)
            print(num-n+1,1,num-n+1,opposite_num)
    else:
        for n in range(2,num//2+1,2):
            if num//2==n:
                print(n,1,n+1,opposite_num)
            else:
                print(n,1,n,opposite_num)
                print(num-n+1,1,num-n+1,opposite_num)
                
def N_odd_func(num,opposite_num):
    for n in range(2,num,2):
        print(n,1,n,opposite_num)

def M_even_func(num,opposite_num):
    if num<=2:
        return
    if (num//2)%2==1:
        for n in range(2,num//2+1,2):
            print(1,n,opposite_num,n)
            print(1,num-n+1,opposite_num,num-n+1)
    else:
        for n in range(2,num//2+1,2):
            if num//2==n:
                print(1,n,opposite_num,n+1)
            else:
                print(1,n,opposite_num,n)
                print(1,num-n+1,opposite_num,num-n+1)        
                
def M_odd_func(num,opposite_num):
    for n in range(2,num,2):
        print(1,n,opposite_num,n)

N, M = list(map(int,input().split()))

if is_even(N) and is_even(M):
    print(count(N)+count(M)+2)
    print(1,M//2+1,N//2,M)
    print(N//2+1,1,N,M//2)
    N_even_func(N,M)
    M_even_func(M,N)
elif is_even(N) and not is_even(M):
    print(count(N)+count(M)+1)
    print(N//2+1,1,N,M)
    N_even_func(N,M)
    M_odd_func(M,N)
elif not is_even(N) and is_even(M):
    print(count(N)+count(M)+1)
    print(1,M//2+1,N,M)    
    N_odd_func(N,M)
    M_even_func(M,N)
else:
    print(count(N)+count(M))
    N_odd_func(N,M)
    M_odd_func(M,N)
    