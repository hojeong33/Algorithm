# 비밀번호 찾기
N, M = map(int, input().split())  # N:저장된 사이트 주소 수 M: 비밀번호를 찾으려는 사이트 주소 수
memo = {}
for i in range(N):
    a, b = input().split()
    memo[a] = b
for i in range(M):
    print(memo[input()])
