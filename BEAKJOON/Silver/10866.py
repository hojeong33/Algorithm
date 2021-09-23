# 덱
from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()
for i in range(N):
    temp = sys.stdin.readline().split()
    s = temp[0]
    if len(temp) == 2:
        if s == 'push_front':
            q.appendleft(temp[1])
        elif s == 'push_back':
            q.append(temp[1])
    else:
        if s == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif s == 'size':
            print(len(q))
        elif len(q) == 0:
            print(-1)
        elif s == 'pop_front':
            print(q.popleft())
        elif s == 'pop_back':
            print(q.pop())
        elif s == 'front':
            print(q[0])
        elif s == 'back':
            print(q[-1])
