x=input()
dic={}
for i in range(26):
    dic[chr(ord("a")+i)]=-1

for i in range(len(x)):
    if dic[x[i]]!=-1:
        continue
    else:
        dic[x[i]]=i

number=0
for key, value in dic.items():
    print(value,end="")
    if number != 25:
        print(" ",end="")