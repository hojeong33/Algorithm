#드래곤 커브
dc = [1, 0, -1, 0]
dr = [0, -1, 0, 1]

n = int(input())
a = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1] + 1) % 4)
        move.extend(temp)
    for i in move:
        nc = x + dc[i]
        nr = y + dr[i]
        a[nc][nr] = 1
        x, y = nc, nr

ans = 0
for i in range(100):
    for j in range(100):
        if a[i][j]:
            if a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
                ans += 1
print(ans)