def f(index):
    if index==0:
        return 0
    elif index==1:
        return 1
    else:
        return f(index-2)+f(index-1)

pibo=int(input())
print(f(pibo))