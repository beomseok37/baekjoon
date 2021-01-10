s=input()
length=len(s)
count=0
index=0
slist=["c=","c-","dz","d-","lj","nj","s=","z="]
flist=["c","d","l","n","s","z"]
while index<length:
    if s[index] in flist:
        if s[index:index+2] in slist:
            if s[index:index+2] == "dz":
                if index+2>=length:
                    count+=2
                    index+=2
                    break
                if s[index+2] == "=":
                    count+=1
                    index+=3
                else:
                    count+=2
                    index+=2
                    continue
            else:
                count+=1
                index+=2
        else:
            count+=1
            index+=1

    else:
        count+=1
        index+=1

print(count)