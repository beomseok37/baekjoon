from itertools import combinations
import sys
input = sys.stdin.readline

def find_array(number):
    result=[int(number)]
    length = len(number)
    where_list = [i for i in range(1,length)]
    
    for count in range(1,length):
        for where in combinations(where_list,count):
            temp=int(number[:where[0]])
            i=1
            while i<count:
                temp+=int(number[where[i-1]:where[i]])
                i+=1
            temp+=int(number[where[-1]:])
            result.append(temp)
    return sorted(result)

def power(array,m):
    result=0
    for value in array:
        result+=value**m
    return result

def find(array,target):
    s,e=0,len(array)-1
    while s<=e:
        m=(s+e)//2
        if array[m]==target:
            return m
        elif array[m]<target:
            s=m+1
        else:
            e=m-1
    return -1

T = int(input())
test_case_list = []
for t in range(T):
    test_case_list.append(input()[:-1])

for test_case in test_case_list:
    for t in test_case:
        if t!='0' and t!='1':
            break
    else:
        print('Hello, BOJ 2023!')
        continue
    array = find_array(test_case)
    count=0
    temp=1
    temp_result=power(list(map(int,test_case)),temp)
    while temp_result<=array[-1]:
        if find(array,temp_result)!=-1:
            count+=1
        temp+=1
        temp_result=power(list(map(int,test_case)),temp)
    print(count)
