#미세먼지안녕
# 입력
from collections import deque
R,C,T=map(int,input().split()) # R:행, C:열, T:초
room=[[]for _ in range(R)]
for i in range(R):
    room[i]=list(map(int,input().split()))

#확산

dr=[1,0,-1,0]
dc=[0,-1,0,1]
check=[[0]*C for _ in range(R)]

def bfs(r,c):
    q=deque()
    q.append((r,c))
    while q:
        r,c=q.popleft()
        cnt=0
        A = room[r][c]
        a = A // 5
        for d in range(4):
            nr=r+dr[d]
            nc=c+dc[d]
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if room[nr][nc]==-1:
                continue
            cnt+=1
            check[nr][nc]+=a
        room[r][c]-=cnt*a


for i in range(R):
    for j in range(C):
        if room[i][j]>0:
            bfs(i,j)
for i in range(R):
    for j in range(C):
        room[i][j]+=check[i][j]
print(room)

