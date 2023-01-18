import sys
input = sys.stdin.readline

T = int(input())
test_case_list = []
for _ in range(T):
    test_case_list.append(list(map(int,list(input())[:-1])))
    
for test_case in test_case_list:
    index = -1
    while index > (-1)*len(test_case) and test_case[index]<=test_case[index-1]:
        index-=1
    
    if abs(index) == len(test_case):
        print('BIGGEST')
        continue
    
    sliced_list = test_case[index-1:]
    sorted_sliced_list = sorted(sliced_list)
    first_num_index = sorted_sliced_list.index(test_case[index-1])
    while sorted_sliced_list[first_num_index] == test_case[index-1]:
        first_num_index+=1
    
    first_num = sorted_sliced_list[first_num_index]
    sorted_sliced_list.pop(first_num_index)
    sorted_sliced_list = [first_num]+sorted_sliced_list
    
    result_list = map(str,test_case[:index-1]+sorted_sliced_list)
    print(''.join(result_list))
