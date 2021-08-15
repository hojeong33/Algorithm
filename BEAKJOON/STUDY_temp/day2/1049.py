#기타줄
N,M=map(int,input().split()) #N,M 입력
min_cost=[] # 묶음, 낱개 각각의 최소값을 저장함
line_list=[] # 브랜드별 가격을 리스트로 받음

for i in range(M): 
    lines=list(map(int,input().split()))
    line_list.append(lines)

# 가격 최소 찾기
min_lines=line_list[0][0]
min_line=line_list[0][1]
for i in range(M):
    if line_list[i][0]<min_lines:
        min_lines=line_list[i][0]
    if line_list[i][1]<min_line:
        min_line=line_list[i][1]
min_cost.append(min_lines) # min_cost 0인덱스에 묶음 최소값
min_cost.append(min_line)  # min_cost 1인덱스에 낱개 최소값

# !!!묶음으로 사는 것이 낱개6개 사는 것보다 저렴할 때!!!
if min_cost[0]<min_cost[1]*6:
    if min_cost[0]<min_cost[1]*(N%6): 
        ans=min_cost[0]*(N//6+1)
    else:
        ans=min_cost[0]*(N//6)+min_cost[1]*(N%6)
else:
    ans=min_cost[1]*N  #낱개로 사는 게 싸다면 낱개 * 개수

print(ans)

