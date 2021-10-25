# 순열 N자리 M진수
n=int(input())
m=int(input())
data=[0]*n
visited=[False]*m

def recur(cur):
    if cur==n:
        print(data)
        return
    for i in range(m):
        if visited[i]:
            continue

        visited[i]=True
        data[cur]=i
        recur(cur+1)
        visited[i]=False

recur(0)

# [0, 1, 2]
# [0, 1, 3]
# [0, 2, 1]
# [0, 2, 3]
# [0, 3, 1]
# [0, 3, 2]
# [1, 0, 2]
# [1, 0, 3]
# [1, 2, 0]
# [1, 2, 3]
# [1, 3, 0]
# [1, 3, 2]
# [2, 0, 1]
# [2, 0, 3]
# [2, 1, 0]
# [2, 1, 3]
# [2, 3, 0]
# [2, 3, 1]
# [3, 0, 1]
# [3, 0, 2]
# [3, 1, 0]
# [3, 1, 2]
# [3, 2, 0]
# [3, 2, 1]

