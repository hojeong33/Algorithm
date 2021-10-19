# 연결 요소의 개수
import sys


def dfs(n):
    visited[n] = 1
    for i in lst[n]:
        if not visited[i]:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    lst[n1].append(n2)
    lst[n2].append(n1)

ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)
