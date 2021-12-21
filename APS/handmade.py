# 예산 안으로 최단거리 및 비용찾기
# 간선 , 노드, 예산 주어줌
# 각 줄에 노드 길이 비용
import random
dist=[10,15,20,25,30,35,40,45,50]
cost=[1500,2000,3000,3500,4000,4500,5000,5500,6000,7000]
for i in range(40):
    node=list(random.sample(range(2,25),2))
    t_d=random.choice(dist)
    t_c=random.choice(cost)
    print(*node,t_d,t_c)
# def Prim():
#     dist = [987654321] * (V + 1)
#     dist2 = [987654321] * (V + 1)
#     visited = [0] * (V + 1)
#
#     dist[0] = 0
#     dist2[0]=0
#
#     for i in range(V):
#         idx = -1
#         val = 987654321
#
#         for j in range(V + 1):
#             if not visited[j] and dist[j] < val:
#                 idx = j
#                 val = dist[j]
#
#         visited[idx] = 1
#         for j in range(V + 1):
#             if not visited[j] and dist[j] > arr[idx][j] + dist[idx]:
#                 dist[j] = arr[idx][j] + dist[idx]
#             if not visited[j] and M >= dist2[j] > arr2[idx][j] + dist2[idx]:
#                 dist2[j] = arr2[idx][j] + dist2[idx]
#
#     return dist2[1]
#
#
# V, E, M = map(int, input().split())  # 정점개수, 간선 개수, 예산
# arr = [[987654321] * (V + 1) for _ in range(V + 1)]
# arr2 = [[987654321] * (V + 1) for _ in range(V + 1)]
#
# for i in range(E):
#     st, ed, d, m = map(int, input().split())
#     arr[st][ed] = d
#     arr[ed][st]=d
#     arr2[st][ed]=m
#     arr2[ed][st]=m
#
# print(Prim())

