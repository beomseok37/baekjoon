num=int(input())

div=2
if num!=1:
    while div<=num:
        if num%div!=0:
            div+=1
            continue
        else:
            print(div)
            num=num//div