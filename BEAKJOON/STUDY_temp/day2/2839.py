#설탕배달
kg=int(input()) # kg을 입력 받음
max_cnt=kg//3 # 3키로봉지로만 넣는다고 가정하여 최대 봉지 수를 저장
flag=False # 이중 포문 탈출을 위한 변수 (false로 초기화 )

for i in range(0,max_cnt+1): #3키로 봉지 
    for j in range(0,max_cnt+1): #5키로 봉지
        if i*3+j*5==kg:  #5키로를 우선으로 순회하여 kg과 맞아떨어질 때를 찾음
            ans=i+j
            flag=True #원하는 값을 찾으면 flag를 True로 바꿔 
            break# for문 하나 탈출
        else:   # kg과 맞아 떨어지지 않으면 -1 
            ans=-1       
    if(flag): # flag는 트루 이기 때문에 
        break # 바깥 for문 탈출
print(ans)