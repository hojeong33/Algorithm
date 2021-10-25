n=int(input())
m=int(input())
data=[]

def recur(cur,cnt):
    if cnt==n:
        print(data)
        return
    if cur==m:
        return
    data.append(cur)
    recur(cur+1,cnt+1)
    data.pop()
    recur(cur+1,cnt)
recur(0,0)

# [0, 1, 2]
# [0, 1, 3]
# [0, 2, 3]
# [1, 2, 3]

