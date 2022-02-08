num=int(input())
array=input().split()
count=0
for i in array:
    isit=0
    check=int(i)
    if check==1:
        isit=1
    else:
        for j in range(2,check):
            if check%j==0:
                isit=1
                break
    if isit==0:
        count+=1
print(count)