# 트리 순회
def pre_order(n):
    if n + 19 != 0:
        print(chr(n + 65), end='')
        pre_order(left[n])
        pre_order(right[n])


def in_order(n):
    if n + 19 != 0:
        in_order(left[n])
        print(chr(n + 65), end='')
        in_order(right[n])


def post_order(n):
    if n + 19 != 0:
        post_order(left[n])
        post_order(right[n])
        print(chr(n + 65), end='')


N = int(input())
left = [0] * N
right = [0] * N
for i in range(N):
    e, l, r = map(ord, input().split())
    left[e - 65] = l - 65
    right[e - 65] = r - 65

pre_order(0)
print()
in_order(0)
print()
post_order(0)
