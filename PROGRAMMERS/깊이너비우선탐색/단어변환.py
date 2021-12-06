from collections import deque
begin="hit"
target="cog"
words=["hot","dot","dog","lot","log","cog"]
l=len(words)
def bfs():
    q=[[begin,1]]
    q=deque(q)
    visited=[0 for _ in range(l)]
    while q:
        t=q.popleft()
        if t[0]==target:
            return t[1]+1
        for i in range(l):
            t_count=0
            for j in range(len(t)):
                if t[0][j]!=words[i][j]:
                    t_count+=1
            if t_count==1 and not visited[i]:
                visited[i]=1
                q.append([words[i],t[1]+1])
if bfs():
    print(bfs())
else:
    print(0)


