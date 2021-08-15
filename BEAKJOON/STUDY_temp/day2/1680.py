# 쓰레기 수거
cnt=int(input())
long=0 # 거리 
ans=[] # 거리 리스트 (출력값)

#입력값// n_list[[거리,쓰레기양]]
for i in range(cnt):
    W,N=map(int,input().split())
    n_list=[]
    for n in range(N):
        n_list.append(list(map(int,input().split())))

#일단 무조건 전체 한바퀴 돌아야함    
    long=n_list[-1][0]*2
#다시 돌아가야하는 위치 구하기    
    num=[]
    total=0 #누적 쓰레기양
    for k in range(N):
        while n_list[k][1]!=0: #해당 지점 쓰레기가 없을 때까지 반복
            total+=n_list[k][1]
            if total==W and k!=N-1: #마지막 지점에서는 쓰레기를 비우고 돌아올 필요가 없기 때문에 제외
                num.append(k)
                n_list[k][1]=0 #지점 쓰레기 수거 완료
                total=0 # 비우기
            elif total>W: #만약 쓰레기를 한 번에 못 실으면 
                num.append(k)
                total=0 #비우고 다시 지점에 도착
            else:
                n_list[k][1]=0 # 용량 넘치지 않으면 지점 통과
    
    for i in num: #돌아가야하는 시점에 접근하여 왕복 길이를 더해줌
        long+=n_list[i][0]*2
    ans.append(long)

print(*ans,sep='\n')
        

