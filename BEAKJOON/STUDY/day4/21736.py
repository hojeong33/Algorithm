#헌내기는 친구가 필요해 # 다시풀어보기
N,M=map(int,input().split())
p_list=[]
# for i in range(3):
#     p_list.append(input().split())
mylist=[list(input()) for _ in range(N)]
# print(p_list.index('I'))
print(mylist)
print([(i,j) for i in range(N) for j in range(M) if mylist[i][j]=="I"])
