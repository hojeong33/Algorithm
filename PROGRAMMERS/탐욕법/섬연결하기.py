costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n=4
arr=[[987654321]*n for _ in range(n)]
for i in range(len(costs)):
    s=costs[i][0]
    e=costs[i][1]
    w=costs[i][2]
    arr[s][e]=w
    arr[e][s]=w

dist=[987654321]*n
visited=[0]*n

dist[0]=0

for i in range(n-1):
    min_idx=-1
    min_value=987654321

    for j in range(n):
        if not visited[j] and dist[j]<min_value:
            min_idx=j
            min_value=dist[j]

    visited[min_idx]=True
    for j in range(n):
        if not visited[j] and dist[j]>dist[min_idx]+arr[min_idx][j]:
            dist[j]=min(arr[min_idx][j],dist[min_idx]+arr[min_idx][j])
print(sum(dist))
