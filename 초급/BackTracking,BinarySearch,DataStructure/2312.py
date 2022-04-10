n = int(input())
testCases = []
for i in range(n):
  number = int(input())
  testCases.append(number)

for testCase in testCases:
  tempTestCase = testCase
  i=2
  while tempTestCase!=1:
    if tempTestCase%i==0:
      count = 0
      while tempTestCase%i==0:
        count+=1
        tempTestCase//=i
      print(str(i)+" "+str(count))
    i+=1
