#수 정렬하기3
import sys
N=int(input())
n=[0]*10001
for i in range(N):
    num=int(sys.stdin.readline())
    n[num]+=1
for i in range(10001):
    k=n[i]
    for j in range(k):
        print(i)
