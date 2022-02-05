#경사로
def check_road(r,c,d):
    global ans
    visited=[0]*N
    if d=='right':
        for i in range(N - 1):
            diff = arr[r][i] - arr[r][i + 1]
            if diff==0:
                pass
            elif diff == 1:
                temp = arr[r][i + 1]
                for j in range(L):
                    if i + 1 + j < N and not visited[i + 1 + j] and arr[r][i + 1 + j] == temp:
                        visited[i + 1 + j] = 1
                    else:
                        return
            elif diff ==-1:
                temp = arr[r][i]
                for j in range(L):
                    if i - j >=0 and not visited[i - j] and arr[r][i - j] == temp:
                        visited[i - j] = 1
                    else:
                        return
            else:
                return

    elif d=='down':
        for i in range(N - 1):
            diff=arr[i][c] - arr[i + 1][c]
            if diff==0:
                pass
            elif diff==1:
                temp = arr[i + 1][c]
                for j in range(L):
                    if i + 1 + j < N and not visited[i + 1 + j] and arr[i + 1 + j][c] == temp:
                        visited[i + 1 + j] = 1
                    else:
                        return
            elif diff ==-1:
                temp = arr[i][c]
                for j in range(L):
                    if i - j >=0 and not visited[i - j] and arr[i -j][c] == temp:
                        visited[i - j] = 1
                    else:
                        return
            else:
                return

    ans+=1
    # print(r,c,d)


N,L=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
ans=0
for r in range(N):
    check_road(r,0,'right')

for c in range(N):
    check_road(0,c,'down')

print(ans)