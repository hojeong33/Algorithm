# 개미
w, h = map(int, input().split())  # w: 가로 h: 세로
x, y = map(int, input().split())  # x:열 y: 행
t = int(input())

w_list = []
h_list = []

for i in range(w):
    w_list.append(i)
for i in range(w, 0, -1):
    w_list.append(i)

for i in range(h):
    h_list.append(i)
for i in range(h, 0, -1):
    h_list.append(i)

ans_x = w_list[(x + t) % (2 * w)]
ans_y = h_list[(y + t) % (2 * h)]
print(ans_x, ans_y)

# 시간 초과
# x와 y좌표를 따로 구하기 x는 좌우로만 y는 상하로만 움직임

# w, h = map(int, input().split())  # w: 가로 h: 세로
# x, y = map(int, input().split())  # x:열 y: 행
# dr = [1, 1, -1, 1]
# dc = [1, -1, -1, -1]
# br = [0, h]
# bc = [0, w]
# d = 0
# t = int(input())
# for i in range(t):
#     if x in bc and y in br:
#         d = (d + 2) % 4
#     elif x in bc or y in br:
#         d = (d + 1) % 4
#     x += dc[d]
#     y += dr[d]
# print(x, y)
