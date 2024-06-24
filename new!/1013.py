T = int(input())
cases = [list(input()) for _ in range(T)]
for case in cases:
    i = 0
    flag = True
    while i+1 < len(case):
        if case[i]+case[i+1] == '01':
            i += 2
        elif i+2 < len(case) and case[i]+case[i+1]+case[i+2] == '100':
            i += 3
            while i < len(case) and case[i] == '0':
                i += 1
            if i == len(case):
                flag = False
                break
            while i < len(case) and case[i] == '1':
                i += 1
        else:
            if i > 2 and case[i-2] == '1' and case[i-1]+case[i] == '10':
                i -= 1
                continue
            flag = False
            break
    if i != len(case) or not flag:
        print('NO')
    else:
        print('YES')
