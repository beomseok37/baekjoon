from itertools import combinations
import sys
input = sys.stdin.readline

def find_distance(mbti1,mbti2):
    result = 0
    for i in range(4):
        if mbti1[i]!=mbti2[i]:
            result+=1
    return result

T = int(input())
test_case_list = []
for _ in range(T):
    N = int(input())
    mbti_list = input().split()
    test_case_list.append([N,mbti_list])
    
for N,mbti_list in test_case_list:
    mbti_object={}
    mbti_set = list(set(mbti_list))
    two_person_mbti_list = []
    result = 100
    flag = False
    
    for mbti in mbti_list:
        if mbti not in mbti_object:
            mbti_object[mbti]=0
        mbti_object[mbti]+=1
        if mbti_object[mbti]==3:
            result=0
            break
    
        if mbti_object[mbti]==2:
            two_person_mbti_list.append(mbti)

    for two_person_mbti in two_person_mbti_list:
        for compare_mbti in mbti_set:
            if two_person_mbti != compare_mbti:
                result = min(result,2*find_distance(two_person_mbti,compare_mbti))
    
    for mbti1,mbti2,mbti3 in combinations(mbti_set,3):
        distance = find_distance(mbti1,mbti2)+find_distance(mbti2,mbti3)+find_distance(mbti3,mbti1)
        result = min(result,distance)
        
    print(result)
