#도로와 신호등
N,L=map(int,input().split()) # N:신호등 개수 L:도로 길이
drg_list=[] #[[위치,빨간색지속,초록색지속],[],[]...]

for i in range(N):
    drg_list.append(list(map(int,input().split()))) #D:신호등 위치 R:빨간색 지속시간, G: 초록색 지속시간
drg_list.append([L,0,0]) #도로의 길이를 다른 리스트와 같은 형식으로 넣음
my_time=drg_list[0][0] #첫 신호등까지의 길이(1초에 1미터니깐 )를 시간에 저장
for i in range(N): #신호등 개수 만큼 순회함
    if my_time%(drg_list[i][1]+drg_list[i][2])<drg_list[i][1]: # 빨간색 지속 5초 , 파란색 지속 5초--> 10초 사이클, 내가 신호등에 도착했을 때 빨간불일때 
        my_time+=drg_list[i][1]-my_time%(drg_list[i][1]+drg_list[i][2]) #남은 빨간불 시간을 더해줌

    my_time+=(drg_list[i+1][0]-drg_list[i][0]) #파란불일때는 다음 신호등까지의 거리를 더해줌,//마지막 신호등일 경우 최종 도로 위치까지 더해줌
    
print(my_time)
