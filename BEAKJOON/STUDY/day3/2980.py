#도로와 신호등
N,L=map(int,input().split()) # N:신호등 개수 L:도로 길이
drg_list=[]

for i in range(N):
    drg_list.append(list(map(int,input().split()))) #D:신호등 위치 R:빨간색 지속시간, G: 초록색 지속시간
drg_list.append([L,0,0])
my_time=drg_list[0][0]
for i in range(N):
    if my_time%(drg_list[i][1]+drg_list[i][2])<drg_list[i][1]:
        my_time+=drg_list[i][1]-my_time%(drg_list[i][1]+drg_list[i][2])

    my_time+=(drg_list[i+1][0]-drg_list[i][0])
    
print(my_time)
