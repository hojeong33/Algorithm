#컨베이어 벨트 위의 로봇
from collections import deque

N,K=map(int,input().split())
A=deque(list(map(int,input().split()))) # 내구도
arr=deque([False]*(2*N)) # 로봇 있으면 true, 없으면 false
up=0 #올리는 곳
down=N-1 #내리는 곳
ans=0 # 가장 처음 수행되는 단계 1
cnt=0

while cnt<K:
    A.rotate(1) # 오른쪽 이동
    arr.rotate(1)
    arr[down]=False # N-1 내림 처리
    for i in range(N-2,-1,-1):
        if arr[i] and not arr[i+1] and A[i+1]:
            A[i+1]-=1
            arr[i+1]=arr[i]
            arr[i]=False
            if not A[i+1]:
                cnt+=1
    arr[down]=False
    if not arr[up] and A[up]:
        A[up]-=1
        arr[up]=True # 새로 올려주기
        if not A[up]:
            cnt+=1
    ans+=1
    
print(ans)









