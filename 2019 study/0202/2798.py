count, limit=map(int,input().split())
blackjack=input().split()
for i in range(len(blackjack)):
    blackjack[i]=int(blackjack[i])
blackjack.sort()
now=0
for first in range(0,count-2):
    for second in range(first+1,count-1):
        for third in range(second+1,count):
            result=blackjack[first]+blackjack[second]+blackjack[third]
            if result>limit:
                break
            if result>now:
                now=result

print(now)