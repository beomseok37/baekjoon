from functools import cmp_to_key
import sys
input = sys.stdin.readline

def compare(value1,value2):
    if value1[1]-value2[1] != 0:
        return value1[1]-value2[1]
    return value1[0]-value2[0]

p = int(input())
test_case_list = []

while p != 0:
    new_test_case = []
    for i in range(p):
        new_test_case.append(list(map(int,input().split())))
    test_case_list.append(new_test_case)
    p = int(input())

for index,test_case in enumerate(test_case_list):
    count = 0
    exist_time_in_party = [0 for _ in range(25)]
    sorted_test_case = sorted(test_case,key=cmp_to_key(compare))
    for start_time,end_time in sorted_test_case:
        for time in range(start_time,end_time):
            if exist_time_in_party[time] < 2:
                exist_time_in_party[time] += 1
                count+=1
                break
    print("On day "+str(index+1)+" Emma can attend as many as "+str(count)+" parties.")
