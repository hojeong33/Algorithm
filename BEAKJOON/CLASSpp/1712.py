#손익분기점
def findPoint():
    A, B, C = map(int, input().split())
    if B > =C:
        cnt = -1
        return -1
    cnt = A // (C-B)
    while A + B * cnt >= C * cnt:
        cnt += 1
    return cnt
print(findPoint())


