# ATM
N = int(input())
waiting = list(map(int, input().split()))
waiting.sort()
sum = 0
ans = 0
for i in waiting:
    sum += i
    ans += sum
print(ans)
