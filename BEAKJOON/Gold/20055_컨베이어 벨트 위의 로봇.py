#컨베이어 벨트 위의 로봇
from collections import deque

N,K=map(int,input().split())
A=deque(list(map(int,input().split()))) # 내구도
arr=deque([False]*(2*N)) # 로봇 있으면 true, 없으면 false
up=0 #올리는 곳
down=N-1 #내리는 곳
ans=1 # 가장 처음 수행되는 단계 1

while 1:
    A.rotate(1) # 오른쪽 이동
    arr.rotate(1)
    arr[down]=False # N-1 내림 처리
    for i in range(N-2,-1,-1):
        if arr[i] and not arr[i+1] and A[i+1]:
            A[i+1]-=1
            arr[i+1]=arr[i]
            arr[i]=False
    arr[down]=False
    if not arr[up] and A[up]:
        A[up]-=1
        arr[up]=True # 새로 올려주기

    cnt=0
    for i in range(2*N):
        if not A[i]:
            cnt+=1
    if cnt>=K:
        break
    else:
        ans+=1
print(ans)









