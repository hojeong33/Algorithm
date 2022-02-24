#탑
def find_top(i):
    temp = tops[i]  # 탑 높이
    while 1:  # 송신 가장 먼저 닫는 곳 찾기
        for j in range(i - 1, 0, -1):
            if temp < tops[j]:
                ans[i] = j + 1
                return
        else:
            ans[i]=0
            return

N=int(input())
tops=list(map(int,input().split()))
ans=[0]*N
for i in range(N - 1, 0, -1):
    find_top(i)
print(*ans)