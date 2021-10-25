# 스타트와 링크
from itertools import combinations

N=int(input())
S=[list(map(int,input().split())) for _ in range(N)]
members=[int(i) for i in range(N)]

ans=99999999
combination=set(combinations(members,N//2))

for team in combination:
    A = 0
    B = 0
    for r in range(N):
        for c in range(N):
            check1=0
            check2=0
            if r in team:
               check1=1
            if c in team:
                check2=1

            if check1==1 and check2==1:
                A+=S[r][c]
            elif check1==0 and check2==0:
                B += S[r][c]

    # 차이 최소값 갱신
    temp = abs(A - B)
    if temp < ans:
        ans = temp
    if temp==0:
        ans=0
        break
print(ans)

