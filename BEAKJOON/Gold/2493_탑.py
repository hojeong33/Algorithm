#탑
N = int(input())  # 탑의 개수
tops = list(map(int, input().split()))
stack = []
ans = []

for i in range(N):
    while stack:
        if stack[-1][1] > tops[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, tops[i]])

print(*ans)






# 시간초과 -> 스택으로 풀기
# def find_top(i):
#     temp = tops[i]  # 탑 높이
#     for j in range(i-1, -1, -1):
#         if temp < tops[j]:
#             ans[i] = j + 1
#             return
#
# N=int(input())
# tops=list(map(int,input().split()))
# ans=[0]*N
#
# for i in range(N - 1, 0, -1):
#     find_top(i)
# print(*ans)