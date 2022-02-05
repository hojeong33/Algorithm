#경사로
def check_road(r,c,d):
    global ans
    visited=[0]*N
    temp=0
    if d=='right':
        for i in range(N - 1):
            if arr[r][i] == arr[r][i + 1]:
                pass
            elif arr[r][i] - arr[r][i + 1] != 1:
                return
            else:
                temp=arr[r][i+1]
                for j in range(L):
                    if i+1+j<N and not visited[i + 1 + j]:
                        visited[i + 1 + j] = 1
                    else:
                        return
    elif d=='down':
        for i in range(N - 1):
            if arr[i][c] == arr[i + 1][c]:
                pass
            elif arr[i][c] - arr[i + 1][c] != 1:
                return
            else:
                temp=arr[i+1][c]
                for j in range(L):
                    if i+1+j<N and not visited[i + 1 + j] and arr[i+1+j][c]==temp:
                        visited[i + 1 + j] = 1
                    else:
                        return

    elif d=='left':
        for i in range(N - 1,0,-1):
            if arr[r][i] == arr[r][i - 1]:
                pass
            elif arr[r][i] - arr[r][i - 1]!=1:
                return
            else:
                for j in range(L):
                    if i-1-j>=0 and not visited[i - 1 - j]:
                        visited[i - 1 +-j] = 1
                    else:
                        return
    else:
        for i in range(N - 1,0,-1):
            if arr[i][c] == arr[i - 1][c]:
                pass
            elif arr[i][c] - arr[i -1][c] !=1:
                return
            else:
                for j in range(L):
                    if i-1-j>=0 and not visited[i - 1 - j]:
                        visited[i - 1 -j] = 1
                    else:
                        return

    ans+=1
    print(r,c,d)


N,L=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
ans=0
for r in range(N):
    if arr[r][0]>=arr[r][N-1]:
        check_road(r,0,'right')
    else:
        check_road(r,N-1,'left')

for c in range(N):
    if arr[0][c]>=arr[N-1][c]:
        check_road(0,c,'down')
    else:
        check_road(N-1,c,'up')
print(ans)