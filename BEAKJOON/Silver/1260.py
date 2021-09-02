# DFS와 BFS
def dfs(V):
    print(V, end=' ')
    v[V] = 1
    g[V].sort()
    for i in g[V]:
        if v[i] == 0:
            v[i] = 1
            dfs(i)
    return


def bfs():
    q = [V]
    v[V] = 1
    print(V, end=' ')
    while q:
        t = q.pop(0)
        g[t].sort()
        for i in g[t]:
            if v[i] == 0:
                v[i] = 1
                print(i, end=' ')
                q.append(i)
    return


N, M, V = map(int, input().split())
g = [[] for _ in range(N + 1)]
v = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dfs(V)
print()
v = [0] * (N + 1)
bfs()
