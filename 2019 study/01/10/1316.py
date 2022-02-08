num=int(input())
l=[]
for i in range(num):
    a=input()
    l.append(a)

count=0
for s in l:
    result=[]
    isit=1
    fixed=s[0]
    result.append(s[0])
    for i in range(1,len(s)):
        if s[i] in result:
            if fixed!=s[i]:
                isit=0
                break
        else:
            result.append(s[i])
            fixed=s[i]
    if isit==1:
        count+=1

print(count)