number=int(input())

check=665
def check666(numbstring):
    for i in range(len(numbstring)-2):
        if numbstring[i]=='6' and numbstring[i+1]=='6' and numbstring[i+2]=='6':
            return True
    return False
numof666=0
while numof666!=number:
    check+=1
    tmp_str=str(check)
    if check666(tmp_str):
        numof666+=1

print(check)