#듣보잡
N,M=map(int,input().split())
N_list=[] #듣도 못한 사람
M_list=[] #보도 못한 사람
for i in range(N): 
    N_list.append(input())
for i in range(M):
    M_list.append(input())

ans=set(N_list)&set(M_list) # set 교집합
print(len(ans))
print(*sorted(ans),sep="\n") #정렬된 set 출력 사전순으로 출력

# 시간초과 

# N,M=map(int,input().split())
# pre_lsit=[]
# ans_list=[]
# for i in range(N+M):
#     name=input()
#     if not(name in pre_lsit):
#         pre_lsit.append(name)
#     else:
#         ans_list.append(name)
# print(len(ans_list))
# print(*ans_list,sep='\n')

# N,M=map(int,input().split())
# N_list=[]
# ans_list=[]
# for i in range(N):
#     N_list.append(input())
# for i in range(M):
#     name=input()
#     if name in N_list:
#         ans_list.append(name)
# print(len(ans_list))
# print(*ans_list,sep='\n')