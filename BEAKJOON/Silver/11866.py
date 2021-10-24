# 요세푸스 문제0
from collections import deque
N,K=map(int,input().split())
lst=[i for i in range(1,N+1)]
lst=deque(lst)
ans=[]
while lst:
    for i in range(K-1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())

print('<',end='')
for i in range(len(ans)-1):
    print(ans[i],end=', ')
print(ans[-1],end='')
print('>')
# N,K =map(int,input().split())
# lst=[i for i in range(1,N+1)]
# ans=[]
# idx=K-1
# if N==1:
#     print('<1>')
# else:
#     if N==K:
#         for i in range(N,0,-1):
#             ans.append(i)
#     else:
#         while lst:
#             if idx>len(lst)-1:
#                 idx-=len(lst)
#             if 1<len(lst)<=K-1:
#                 idx%=(K-1)
#             if len(lst)==1:
#                 idx=0
#             ans.append(lst.pop(idx))
#             idx+=K-1
#     print('<',end='')
#     for i in range(len(ans)-1):
#         print(ans[i],end=', ')
#     print(ans[-1],end='')
#     print('>')