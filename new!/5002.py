import sys
input = sys.stdin.readline

def to_num(string):
    return 1 if string=='M' else -1

def choose_between_fronts(difference):
    first_person_difference = order[0]+difference
    second_person_difference = order[1]+difference
    
    if abs(first_person_difference)<=abs(second_person_difference):
        order.pop(0)
        return first_person_difference
    else:
        order.pop(1)
        return second_person_difference

X = int(input())
order = list(map(to_num,list(input())[:-1]))
difference = 0
count = 0

while len(order)>1:
    difference = choose_between_fronts(difference)
    
    if abs(difference)>X:
        break
    
    count+=1

if difference<=X and abs(difference+order[-1])<=X:
    count+=1
    
print(count)
