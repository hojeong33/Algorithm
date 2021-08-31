# 수 정렬하기2
import sys
N=int(input())
n=[int(sys.stdin.readline()) for _ in range(N)]
n.sort()
for i in n:
    print(i)
