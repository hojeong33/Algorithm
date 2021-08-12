#달팽이
N=int(input())
box=[[0]*N for _ in range(N)]
key=int(input())
#시작 좌표
r=(N//2)
c=(N//2)
num=1
#방향
dr=[-1,0,1,0] # 상 우 하 좌
dc=[0,1,0,-1]
d=0 #방향인덱스
k=2 #방향 지속 컨트롤


#위로 하나,옆으로 하나, 밑으로 두개, 옆으로 두개, 위로 세개....
while num<=N*N:
    cnt=0
    while cnt<(k//2): # 1,1,2,2,3,3,4,4로 나오게 하기 위해서 2로 나눔
        if 0<=r<N and 0<=c<N:
            box[r][c]=num
        if num==key:
            ans=[r,c]
        num+=1
        r+=dr[d]
        c+=dc[d]
        cnt+=1
    d = (d + 1) % 4 #방향 바꿔줌
    k+=1

# 출력
for i in range(N):
    for j in range(N):
        print('{}'.format(box[i][j]),end=' ')
    print()
print('{} {}'.format(ans[0]+1,ans[1]+1))


