#감시

from collections import deque

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def check(cnt):
    global ans,bang2
    if cnt==cctv:
        tmp=0
        for i in range(N):
            for j in range(M):
                if not bang[i][j] and not bang2[i][j]:
                    tmp+=1
        return tmp
    r,c=cc[cnt][0],cc[cnt][1]
    for d in range(4):
        directions = []
        if bang[r][c]==1:
            directions.append(d)
        elif bang[r][c]==2:
            directions.append(d)
            directions.append((d+2)%4)
        elif bang[r][c]==3:
            directions.append(d)
            directions.append((d-1)%4)
        elif bang[r][c]==4:
            directions.append(d)
            directions.append((d -1) % 4)
            directions.append((d + 2) % 4)
        elif bang[r][c]==5:
            directions.append(d)
            directions.append((d-1)%4)
            directions.append((d+1)%4)
            directions.append((d+2)%4)
        q=deque()
        for k in directions:
            nr,nc=r+dr[k],c+dc[k]
            while 0<=nr<N and 0<=nc<M:
                if not bang2[nr][nc] and bang[nr][nc] != 6:
                    bang2[nr][nc] = True
                    q.append((nr, nc))
                elif bang[nr][nc] == 6:
                    break
                nr+=dr[k]
                nc+=dc[k]
        ans=min(ans,check(cnt+1))
        while q:
            pr,pc=q.popleft()
            if not bang[pr][pc]:
                bang2[pr][pc] = False
        if bang[r][c]==5:
            break
    return ans

#입력
N,M=map(int,input().split())
bang=[[]for _ in range(N)]
for i in range(N):
    bang[i]=list(map(int,input().split()))

# cctv 개수
cctv=0
cc=[]
for i in range(N):
    for j in range(M):
        if 0<bang[i][j]<6:
            cctv+=1
            cc.append((i,j))
        if bang[i][j]==0:
            ans+=1
ans= 987654321 #사각지대 초깃값
bang2=[[False]*M for _ in range(N)]
check(0)
print(ans)


