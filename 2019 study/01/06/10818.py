num=int(input())
n=input()
li=n.split(' ')
result=[]
for i in range(num):
    result.append(int(li[i]))
result.sort()
print(result[0],result[-1])