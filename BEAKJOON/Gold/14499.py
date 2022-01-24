#주사위 굴리기

#동-서-북-남
dr=[0,0,-1,1]
dc=[1,-1,0,0]

N,M,x,y,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
order=list(map(int,input().split()))
dice=[0 for _ in range(6)]

#위 북 동 서 남 아래

for i in range(K):
    d=order[i]-1 # 인덱스로
    nr=x+dr[d]
    nc=y+dc[d]
    if 0>nr or 0>nc or nr>=N or nc>=M: #범위밖이면
        continue
    # 동쪽,서쪽으로 이동시 북,남은 변화 없음
    if d==0:#동쪽
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif d==1:#서쪽
        dice[0], dice[2], dice[3], dice[5] =dice[2],dice[5],dice[0],dice[3]
    # 북쪽,남쪽 이동시 동,서는 변화 없음
    elif d==2:#북쪽
        dice[0],dice[1],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[1]
    elif d==3:#남쪽
        dice[0], dice[1], dice[4], dice[5] = dice[1],dice[5],dice[0],dice[4]
    if arr[nr][nc]==0: #주사위 바닥 복사
        arr[nr][nc]=dice[5]
    else:
        dice[5]=arr[nr][nc] # 칸 복사
        arr[nr][nc]=0 # 칸 0초기화

    x,y=nr,nc
    print(dice[0])

