from collections import deque
tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets.sort(key=lambda x:x[1])
print(tickets)
def bfs():
    q=["ICN"]
    route=["ICN"]
    q=deque(q)
    l=len(tickets)
    visited=[0 for _ in range(l)]
    while q:
        t=q.popleft()
        for i in range(l):
            if tickets[i][0]==t and not visited[i]:
                visited[i]=1
                q.append(tickets[i][1])
                route.append(tickets[i][1])
                break
    print(route)
bfs()

