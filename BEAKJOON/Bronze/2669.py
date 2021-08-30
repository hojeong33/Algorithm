# 직사각형 네개의 합집합의 면적 구하기
box=[[0]*100 for _ in range(100)]
for i in range(4):
    l_x,l_y,r_x,r_y=map(int,input().split())
    for r in range(l_y,r_y):
        for c in range(l_x,r_x):
            box[r][c]=1
cnt=0
for i in range(100):
    for j in range(100):
        if box[i][j]==1:
            cnt+=1
print(cnt)