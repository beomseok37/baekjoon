def findCount(array,number):
  first = 0
  last = len(array)-1
  while first<last:
    mid = (first+last)//2
    if array[mid]==number:
      while mid<len(array) and array[mid]==number:
        mid+=1
      return mid
    elif array[mid]>number:
      last=mid-1
    else:
      first=mid+1
  return first if array[first]>number else first+1


testCount = int(input())
for i in range(testCount):
  answer = 0
  n,m=list(map(int,input().split()))
  a=sorted(list(map(int,input().split())))
  b=sorted(list(map(int,input().split())))
  for number in b:
    index = findCount(a,number)
    answer+= len(a)-index
  print(answer)
