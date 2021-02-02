number=int(input())
person=[]
for i in range(number):
    weight, height=map(int,input().split())
    bulk={}
    bulk["weight"]=weight
    bulk["height"]=height
    bulk["bigger"]=1
    person.append(bulk)

for front in range(number-1):
    for back in range(front+1,number):
        if person[front]["weight"]>person[back]["weight"] and person[front]["height"]>person[back]["height"]:
            person[back]["bigger"]+=1
        if person[front]["weight"]<person[back]["weight"] and person[front]["height"]<person[back]["height"]:
            person[front]["bigger"]+=1
for i in range(number):
    print(person[i]["bigger"],end=" ")

#순위를 매겨야 되는줄 알고 잘 못 설계함
# bigger=[]
# for i in range(number):
#     bigger.append(person[i]["bigger"])
# bigger.append(-1)
# bigger.sort(reverse=True)
# count=1
# rate=1
# rate_dic={}
# for i in range(number):
#     if bigger[i]!=bigger[i+1]:
#         rate_dic[bigger[i]]=rate
#         rate+=count
#         count=1
#     else:
#         count+=1
# for i in range(number-1):
#     print(rate_dic[person[i]["bigger"]],end=" ")
# print(rate_dic[person[-1]["bigger"]])