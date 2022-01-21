#아기 상어
from collections import deque

dr=[-1,0,1,0]
dc=[0,1,0,-1]

#입력
N=int(input())
arr=[list(map(int,input().split()))for _ in range(N)]


# 상어 위치 찾기
for r in range(N):
    for c in range(N):
        if arr[r][c]==9:
            start=[r,c]
            arr[r][c]=0
            break

ans=0 # 시간
size=2 # 가장 처음의 아기 상어의 크기
eat=0 # 물고기 먹은 수

while 1:
    q=deque()
    q.append((start[0],start[1],0)) # 상어 r, 상어 c, 이동횟수
    visited=[[False]*N for _ in range(N)]
    flag=987654321
    fish=[] # 먹을 수 있는 물고기
    while q:
        r,c,cnt=q.popleft()
        if cnt>flag:
            break
        for d in range(4):
            nr,nc=r+dr[d],c+dc[d]
            if nr<0 or nr>=N or nc<0 or nc>=N: # 범위체크
                continue
            if arr[nr][nc]>size or visited[nr][nc]: #사이즈, 방문 체크
                continue
            if 0<arr[nr][nc]<size: # 상어보다 사이즈 작은 물고기 이면
                fish.append((cnt+1,nr,nc))
                flag=cnt
            visited[nr][nc]=True #방문체크
            q.append((nr,nc,cnt+1))

    if len(fish)>0:
        fish.sort()
        m,r,c=fish[0][0],fish[0][1],fish[0][2]
        ans+=m
        eat+=1
        arr[r][c]=0
        if eat==size:
            size+=1
            eat=0
        start=[r,c]
    else:
        break
print(ans)

# 이차원 리스트 정렬 하나만 지정시 그 하나만 기준으로 정렬 됨
a=[[1,2],[2,3],[2,1],[1,3]]
a.sort()
print(a)
a.sort(key=lambda x:x[1])
print(a)
a.sort(key=lambda x:x[0])
print(a)
a.sort(key=lambda x:(x[1],x[0]))
print(a)
