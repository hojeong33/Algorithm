# 회전하는 큐
from collections import deque

N, M = map(int, input().split())
points = list(map(int, input().split()))
q = deque([int(i) for i in range(1, N + 1)])
cnt = 0
ans = 0
while cnt < M:
    for i in points:
        if q.index(i) > len(q) // 2:
            while 1:
                g = q.pop()
                if i == g:
                    cnt += 1
                    ans += 1
                    break
                else:
                    q.appendleft(g)
                    ans += 1
        else:
            while 1:
                k = q.popleft()
                if i == k:
                    cnt += 1
                    break
                else:
                    q.append(k)
                    ans += 1
print(ans)
