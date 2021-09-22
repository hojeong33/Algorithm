# 구간 합 구하기4
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sums = [0]
total = 0
for i in nums:
    total += i
    sums.append(total)
for i in range(M):
    st, ed = map(int, sys.stdin.readline().split())
    print(sums[ed] - sums[st - 1])
