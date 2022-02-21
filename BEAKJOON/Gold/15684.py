#사다리조작
N,M,H=map(int,input().split()) # 세로, 가로, 세로선마다 놓을 수 있는 위치의 개수
for _ in range(M):
    a,b=map(int,input().split()) # b b+1(세로선 왼쪽에서부터 1)  연결 a 점선(1번~)위치에서 연결
if M==0:
    print(0)
else:

