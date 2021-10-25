n=int(input())
m=int(input())
data=[0]*n

def recur(cur,start):
    if cur==n:
        print(data)
        return
    for i in range(start,m):
        data[cur]=i
        recur(cur+1,i+1)
recur(0,0)
# [0, 1, 2]
# [0, 1, 3]
# [0, 2, 3]
# [1, 2, 3]