import time

N, M, X = map(int, input().split())
start = time.time()
bus = [[] for _ in range(N+2)]
for _ in range(M):
    a, b, t, c = map(int, input().split())
    bus[a].append([b, t, c])
    bus[b].append([a, t, c])

temp_distance = temp_cost = float('inf')
visit = [True] + [False] * (N+1)

def dfs(now, distance, cost):
    global temp_distance, temp_cost

    if temp_distance < distance:
        return
    if X < cost:
        return
    if now == 1:
        temp_distance = distance
        temp_cost = cost
        return

    for next_vertex, next_distance, next_cost in bus[now]:
        if visit[next_vertex]:
            continue
        visit[next_vertex] = True
        dfs(next_vertex, distance+next_distance, cost+next_cost)
        visit[next_vertex] = False

dfs(0, 0, 0)
print(temp_distance, temp_cost)
plane_distance, plane_cost = map(int, input().split())
ship_distance, ship_cost = map(int, input().split())
ans_distance = ans_cost = float('inf')
for d, c in [[temp_distance, temp_cost], [plane_distance, plane_cost], [ship_distance, ship_cost]]:
    if d < ans_distance:
        ans_distance = d
        ans_cost = c
    elif d == ans_distance:
        if c < ans_cost:
            ans_cost = c

print(ans_distance, ans_cost)

print(time.time() - start)



# 5 6 5000
# 0 2 10 1000
# 0 3 15 2000
# 3 4 20 1700
# 4 1 10 1000
# 2 1 20 4000
# 2 4 10 1000
# 20 6000
# 30 5000
#
# 30 3000
#
# 5 6 6500
# 0 2 7 2600
# 2 3 5 2000
# 2 4 15 2100
# 3 4 8 2500
# 3 1 20 1400
# 4 1 10 1300
# 20 7000
# 40 6000
#
# 32 6000
#
# 6 9 10000
# 0 2 20 3000
# 0 3 40 2000
# 2 3 30 1000
# 4 5 20 3000
# 2 4 20 3000
# 3 4 30 2000
# 3 5 20 4000
# 5 1 30 2000
# 4 1 10 4000
# 30 12000
# 40 10000
#
# 40 10000
#
# 7 11 15000
# 0 6 10 6000
# 6 4 40 3000
# 6 5 10 5000
# 0 2 30 3000
# 0 3 20 4000
# 3 4 50 5000
# 3 2 10 5000
# 2 4 20 4000
# 4 1 10 3000
# 4 5 10 1000
# 5 1 20 2000
# 60 14000
# 70 12000
#
# 40 13000
#
# 7 11 10000
# 0 6 10 3000
# 6 3 20 4000
# 6 5 10 3000
# 0 2 30 5200
# 0 3 40 3300
# 3 4 30 4000
# 3 2 10 3800
# 2 4 20 4000
# 3 1 20 3500
# 4 5 10 4000
# 5 1 20 3000
# 50 11000
# 80 8000
#
# 40 9000


