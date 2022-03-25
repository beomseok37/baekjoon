a,b,d = list(map(int,input().split()))
d = str(d)

numbers = [False,True] + [True]*(b-1)
answer = 0

for number in range(2,b+1):
  if numbers[number]:
    temp = number*2

    while temp <= b:
      numbers[temp] = False
      temp += number

    if number >= a and d in str(number):
      answer += 1

print(answer)
