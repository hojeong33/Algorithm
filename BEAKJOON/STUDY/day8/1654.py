#랜선 자르기
import sys
K,N=map(int,input().split()) # K: 이미 가지고 있는 랜선의 개수 N:필요한 랜선 개수
line=[int(sys.stdin.readline()) for _ in range(K)] #랜선 길이
line.sort() # 오름차순 정렬
start=1 # zerodivision
end=line[-1] # 가장 큰 수

while 1:
    middle=(start+end)//2
    total=0 # 자른 랜선 개수
    for i in line:
        total+=i//middle
    if total>=N:
        start=middle+1
    else:
        end=middle-1
    print(total,middle)
    if start>end:
        break

print(end)
