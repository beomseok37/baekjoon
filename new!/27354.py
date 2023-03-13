import sys
input = sys.stdin.readline

T=int(input())
test_case_list=[]
for i in range(T):
    t=int(input())
    t_s=input()
    test_case_list.append([t,t_s])
    
for t,t_s in test_case_list:
    one_min,zero_min=[],[]
    one_min_count,zero_min_count=t,t
    zero_flag=t_s[0]=='0'
    s,e=0,0
    for i in range(1,t):
        if zero_flag and t_s[i]=='0':
            e+=1
        elif zero_flag and t_s[i]=='1':
            if zero_min_count==e-s+1:
                zero_min.append([s,e])
            elif zero_min_count>e-s+1:
                zero_min=[[s,e]]
                zero_min_count=e-s+1
            s,e=i,i
            zero_flag=False
        elif not zero_flag and t_s[i]=='1':
            e+=1
        else:
            if one_min_count==e-s+1:
                one_min.append([s,e])
            elif one_min_count>e-s+1:
                one_min=[[s,e]]
                one_min_count=e-s+1
            s,e=i,i
            zero_flag=True
    if s != e:
        if t_s[e]=='1':
            if one_min_count==e-s+1:
                one_min.append([s,e])
            elif one_min_count>e-s+1:
                one_min=[[s,e]]
                one_min_count=e-s+1
        else:
            if zero_min_count==e-s+1:
                zero_min.append([s,e])
            elif zero_min_count>e-s+1:
                zero_min=[[s,e]]
                zero_min_count=e-s+1

    if one_min_count==zero_min_count:
        print(0)
    elif one_min_count<zero_min_count:
        temp=t_s[:]
        