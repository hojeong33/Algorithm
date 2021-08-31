#좌표 정렬하기2
import sys
N=int(input())
n=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
n.sort(key=lambda x:(x[1],x[0]))
for i in range(N):
    print(*n[i])