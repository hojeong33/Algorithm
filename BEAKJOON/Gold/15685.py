#드래곤 커브
dc = [1, 0, -1, 0]
dr = [0, -1, 0, 1]

N = int(input())
miro = [[0]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    miro[x][y] = 1
    c = [d]
    for _ in range(g):
        temp = []
        for i in range(len(c)):
            temp.append((c[-i-1] + 1) % 4)
        c.extend(temp)
        # print(c)
    for i in c:
        nc = x + dc[i]
        nr = y + dr[i]
        miro[nc][nr] = 1
        x, y = nc, nr

# 사각형 꼭짓점이 모두 1이면 ans+=1
ans = 0
for i in range(100):
    for j in range(100):
        if miro[i][j]:
            if miro[i+1][j] and miro[i][j+1] and miro[i+1][j+1]:
                ans += 1
print(ans)