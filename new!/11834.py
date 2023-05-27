n=int(input())
i,temp,result=1,1,0
while i<n:
    result+=1+(temp-1)*2
    temp+=1
    i+=temp

i-=temp
result+=1+(n-i-1)*2
print(result)
