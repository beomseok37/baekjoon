import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
result=0

cards.sort()

while len(cards)!=1:
    card1,card2 = cards.pop(0),cards.pop(0)
    temp = card1+card2
    result+=temp
    
    s,e=0,len(cards)-1
    while s<=e:
        middle = (s+e)//2
        if cards[middle]==temp:
            break
        elif cards[middle]<temp:
            s=middle+1
        else:
            e=middle-1

    if cards and cards[middle]<temp:
        middle+=1
    cards.insert(middle,card1+card2)
    
print(result)
