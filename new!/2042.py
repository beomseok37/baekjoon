import sys
input = sys.stdin.readline

def recursion(start,end,node):
    if start==end:
        segTree[node]=arr[start]
    else:
        mid=(start+end)//2
        segTree[node]=recursion(start,mid,node*2)+recursion(mid+1,end,node*2+1)
    return segTree[node]

def change(start,end,node,target,num):
    if start==end:
        segTree[node]=num
        return segTree[node]
    
    mid=(start+end)//2
    
    if start<=target<=mid:
        segTree[node]=change(start,mid,node*2,target,num)+(segTree[node*2+1] if node*2+1<N*4 else 0)
    elif mid+1<=target<=end:
        segTree[node]=change(mid+1,end,node*2+1,target,num)+(segTree[node*2] if node*2<N*4 else 0)
    
    return segTree[node]

def findSum(targetStart,targetEnd,start,end,node):
    if start==end or (start>=targetStart and end<=targetEnd):
        return segTree[node]
    
    returnValue=0
    mid=(start+end)//2
    
    if targetStart<=mid:
        returnValue+=findSum(targetStart,targetEnd,start,mid,node*2)
    if mid+1<=targetEnd:
        returnValue+=findSum(targetStart,targetEnd,mid+1,end,node*2+1)
    
    return returnValue

N,M,K=list(map(int,input().split()))
arr = [int(input()) for _ in range(N)]
orderList = [list(map(int,input().split())) for _ in range(M+K)]
segTree=[0 for _ in range(N*4)]

recursion(0,N-1,1)
for a,b,c in orderList:
    if a==1:
        change(0,N-1,1,b-1,c)
    else:
        print(findSum(b-1,c-1,0,N-1,1))
