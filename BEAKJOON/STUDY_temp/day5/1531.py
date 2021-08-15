#투명
N,M=map(int,input().split())
painting = []

#2차원 빈 리스트 만들기
for i in range(101):
    line = []
    for j in range(101):
        line.append(0)
    painting.append(line)

#헤당 범위의 인덱스에 +=1 해주기
for i in range(N):
    l_x,l_y,r_x,r_y=map(int,input().split())
    for i in range(l_x,r_x+1):
        for j in range(l_y,r_y+1):
            painting[j][i]+=1

#M보다 큰 경우 카운팅
cnt=0
for i in range(101):
    for j in range(101):
        if painting[j][i]>M:
            cnt+=1
print(cnt)

#테스트 입력값
# 3 1
# 21 21 80 80
# 41 41 60 60
# 71 71 90 90
#출력값
#500