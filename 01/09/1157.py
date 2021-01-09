string=input()
slist=[]
for i in range(len(string)):
    if 97 <= ord(string[i]) <=122:
        slist.append(chr(ord(string[i])-32))
    else:
        slist.append(string[i])

dic={}
for i in slist:
    if i in dic.keys():
        dic[i]=dic[i]+1
    else:
        dic[i]=1

Max=0
isit=0
for key, value in dic.items():
    if value>Max:
        Max=value
        which=key
        isit=0
    elif value==Max:
        isit=1
if isit==0:
    print(which)
else:
    print("?")
