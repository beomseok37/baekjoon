number=input()
number_length=len(number)
number=int(number)
result=0
if number_length==1:
    if number%2==0:
        result=number//2
else:
    range_front=number-number_length*9
    if range_front<0:
        range_front=0
    for num in range(range_front,number):
        digit=num
        digit_list=[]
        while digit!=0:
            one=digit%10
            digit=digit//10
            digit_list.append(one)
        decomposition=num
        for d in digit_list:
            decomposition+=d
        if decomposition==number:
            result=num
            break

print(result)