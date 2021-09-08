# 수 찾기
N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
lst = list(map(int, input().split()))


def check(start, end):
    if start > end:
        return 0
    middle = (start + end) // 2
    mid = nums[middle]
    if m == mid:
        return 1
    elif m < mid:
        return check(start, middle - 1)
    else:
        return check(middle + 1, end)

for m in lst:
    print(check(0,N-1))
