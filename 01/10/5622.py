s=input()
dial=0
for i in range(len(s)):
    x=(ord(s[i])-ord('A'))//3+3
    if 9<=x<11:
        if (ord(s[i])-ord('A'))%3==0:
            x-=1
    elif x==11:
        x-=1
    dial+=x
print(dial)