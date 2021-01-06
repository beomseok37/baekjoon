dic={}
for i in range(10):
    num=int(input())
    num%=42
    dic[num]=1
print(len(dic))