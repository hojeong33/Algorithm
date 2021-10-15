# 주사위 쌓기
def check(idx):
    if idx==0:
        return 5
    if idx==1:
        return 3
    if idx==2:
        return 4
    if idx==3:
        return 1
    if idx==4:
        return 2
    if idx==5:
        return 0

N=int(input())
dice=[list(map(int,input().split())) for _ in range(N)]
# 0번-5번, 1번-3번, 2번-4번, 3번-1번, 4번-2번, 5번-0번
ans=0
for i in range(6):
    result=[]
    temp=[1,2,3,4,5,6]
    temp.remove(dice[0][i])
    up=dice[0][check(i)]
    temp.remove(up)
    result.append(max(temp))
    for j in range(1,N):
        temp=[1,2,3,4,5,6]
        temp.remove(up)
        up=dice[j][check(dice[j].index(up))]
        temp.remove(up)
        result.append(max(temp))
    result=sum(result)
    if ans<result:
        ans=result
print(ans)