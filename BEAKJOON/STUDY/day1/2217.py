# 로프

N = int(input())  # 로프 줄 수
W = []
for i in range(N):
    W.append(int(input()))
W.sort()
max_w = 0
cnt=N
for i in W:
    if max_w < i * cnt:
        max_w = i * cnt
    cnt -= 1
print(max_w)
