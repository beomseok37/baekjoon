import sys
input = sys.stdin.readline

def find(value):
    a,b=0,len(prime_list)-1
    while a<b:
        index = (a+b)//2
        if prime_list[index] == value:
            return index
        elif prime_list[index] < value:
            a=index + 1
        else:
            b=index - 1
    return a

n = int(input())
ab_list = []
prime = [True for i in range(100001)]
prime_list=[2,3]
prefix_sum1=[6,3]
prefix_sum2=[0,9]
max_number = 0

prime[1]=False

for i in range(n):
    a,b = list(map(int,input().split()))
    ab_list.append([a,b])
    max_number = max(max(a,b),max_number)
    
i=2
while i**2 <= max_number:
    multiple = i
    while i*multiple <= max_number:
        prime[i*multiple]=False
        multiple+=1
    i+=1

for i in range(5,max_number+1):
    if prime[i]:
        prime_list.append(i)
        
        if len(prime_list)%2==1:
            prefix_sum1.append(prefix_sum1[-1]+3*i)
            prefix_sum2.append(prefix_sum2[-1]-i)
        else:
            prefix_sum1.append(prefix_sum1[-1]-i)
            prefix_sum2.append(prefix_sum2[-1]+3*i)

for a,b in ab_list:
    if a==1 and b==1:
        print(0)
        continue
    count=0
    a_index,b_index = find(a),find(b)
    if prime_list[a_index]<a:
        a_index+=1
    if prime_list[b_index]>b:
        b_index-=1
        
    if a_index%2==0:
        if a_index==0:
            print(prefix_sum1[b_index])
        else:
            a_index = a_index-1
            print(prefix_sum1[b_index]-prefix_sum1[a_index])
    else:
        if a_index==1:
            print(prefix_sum2[b_index])
        else:
            a_index = a_index - 1
            print(prefix_sum2[b_index]-prefix_sum2[a_index])
