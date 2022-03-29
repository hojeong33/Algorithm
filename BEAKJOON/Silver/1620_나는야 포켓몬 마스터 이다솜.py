import sys
input=sys.stdin.readline
# 인풋이 천개만큼 많을때 쓰세요!
N,M=map(int,input().split())
nameList=[]
nameDict={}
for i in range(N):
    name=input().rstrip()
    nameList.append(name)
    nameDict[name]=i+1
for i in range(M):
    temp=input().rstrip()
    try:
        temp=int(temp)
        print(nameList[temp-1])
    except:
        print(nameDict[temp])