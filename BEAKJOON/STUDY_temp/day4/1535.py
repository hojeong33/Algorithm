#안녕 -다시 풀어보기
N=int(input())
L_list=[int(x) for x in input().split()]
J_list=[int(y) for y in input().split()]
h=100
J=0
while h>0:
    a=J_list.index(max(J_list))
    h-=L_list(a)
    J+=max(J_list)
    J_list.pop(a)
    L_list.pop(a)

