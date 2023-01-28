import sys
input = sys.stdin.readline

T = int(input())
test_case_list = []
number_array = [('Z','ZERO',0),('X','SIX',6),('G','EIGHT',8),('S','SEVEN',7),('V','FIVE',5),('F','FOUR',4),('I','NINE',9),('W','TWO',2),('R','THREE',3),('O','ONE',1)]

for _ in range(T):
    test_case_list.append(list(input())[:-1])

for index,test_case in enumerate(test_case_list):
    test_case_dict = {}
    array = [0]*10
    for w in test_case:
        if w not in test_case_dict:
            test_case_dict[w]=0
        test_case_dict[w]+=1
    
    for letter,word,num in number_array:
        if letter in test_case_dict and test_case_dict[letter]>0:
            array[num] = test_case_dict[letter]
            for w in word:
                test_case_dict[w]-=array[num]
        array[num]=str(num)*array[num]
    print(f"Case #{index+1}: {''.join(array)}")
