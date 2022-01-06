# 인구 이동
from collections import deque
dr=[0,1,0,-1]
dc=[1,0,-1,0]

def bfs(r,c):
    visited[r][c]=1
    q=deque([(r,c)])
    # q.append((r,c))
    check=[(r,c)]
    while q:
        r,c=q.popleft()
        for d in range(4):
            nr=r+dr[d]
            nc=c+dc[d]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc]:
                continue
            if L<=abs(A[nr][nc]-A[r][c])<=R:
                visited[nr][nc]=1
                q.append((nr,nc))
                check.append((nr,nc))
    return check
N,L,R=map(int,input().split()) # N: 크기 L: 이상 R:이하

A=[[] for _ in range(N)]
for i in range(N):
    A[i]=list(map(int,input().split()))

ans=0
is_change=True
while is_change:
    is_change=False
    visited=[[False]*N for _  in range(N)]
    nation=[]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                nation.append(bfs(i,j))

    for i in range(len(nation)):
        total=0
        for j in range(len(nation[i])):
            total+=A[nation[i][j][0]][nation[i][j][1]]
        average=total//len(nation[i])
        while nation[i]:
            r,c=nation[i].pop()
            if A[r][c] !=average:
                is_change=True
                A[r][c]=average
    if is_change:
        ans+=1
print(ans)

