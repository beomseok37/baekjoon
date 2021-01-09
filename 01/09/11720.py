def find(a):
    total=0
    while a>0:
        total+=a%10
        a=a//10
    return total

num=int(input())
array=int(input())
print(find(array))