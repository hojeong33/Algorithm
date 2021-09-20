# 패션왕 신해빈
T = int(input())  # 테스트 케이스 수
for tc in range(T):
    n = int(input())  # 의상 수
    fa = {}
    for i in range(n):
        a, b = input().split()
        if b in fa:
            fa[b] += 1
        else:
            fa[b] = 1
    l = len(fa)
    if l == 1:
        print(n)
    else:
        ans = 1
        for i in fa.values():
            ans *= (i + 1)
        print(ans - 1)
