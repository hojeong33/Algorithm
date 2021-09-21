# 동전 0
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
ans = 0
for i in coins:
    if i > K:
        continue
    else:
        ans += K // i
        K = K % i

print(ans)
