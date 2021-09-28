# 에디터
import sys

s=list(sys.stdin.readline().strip())
N=len(s)
M=int(sys.stdin.readline())
stack=[]
for i in range(M):
    order=sys.stdin.readline().split()
    if order[0]=='L' and s:
        stack.append(s.pop())
    elif order[0]=='D' and stack:
        s.append(stack.pop())
    elif order[0]=='B' and s:
        s.pop()
    elif order[0]=='P':
        s.append(order[1])
s+=stack[::-1]
print(''.join(s))

# import sys
# s = sys.stdin.readline()  # 문자 입력
# cursor = len(s)
# M = int(sys.stdin.readline())  # 명령어 개수
# for i in range(M):
#     t = sys.stdin.readline().split()
#     r_s=s[cursor:]
#     if t[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
#     if t[0] == 'D':
#         if cursor != len(s):
#             cursor += 1
#     if t[0] == 'B' and cursor != 0:
#         s = s[0:cursor - 1] + s[cursor:]
#         cursor -= 1
#     if t[0] == 'P':
#         s = s[0:cursor] + t[1] + s[cursor:]
#         cursor += 1
# print(s)
