factorial=int(input())
result=1
if factorial!=0:
    for i in range(1,factorial+1):
        result*=i
    print(result)
else:
    print(1)