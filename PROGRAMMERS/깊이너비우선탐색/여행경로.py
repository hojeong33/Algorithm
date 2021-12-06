from collections import deque
from copy import deepcopy
# tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets=[["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# ["ICN", "B", "ICN", "A", "D", "A"]
tickets.sort(key=lambda x:x[1])
def bfs():
    q=deque()
    l = len(tickets)
    q.append(("ICN",["ICN"],[0 for _ in range(l)]))
    while q:
        dst,route,visited = q.popleft()
        if len(route)==l+1:
            print(route)
        for i in range(l):
            if tickets[i][0] == dst and not visited[i]:
                visited[i] = 1
                newvisited=deepcopy(visited)
                q.append((tickets[i][1],route+[tickets[i][1]],newvisited))
                visited[i]=0
bfs()

