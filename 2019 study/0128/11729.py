def func(num):
    if num==1:
        return 1
    else:
        return 2*func(num-1)+1

N=int(input())
print(func(N))
def hanoi(num,a,b,c):
    if num==1:
        print(a+" "+c)
    else:
        hanoi(num-1,a,c,b)
        print(a+" "+c)
        hanoi(num-1,b,a,c)
hanoi(N,"1","2","3")