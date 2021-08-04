#영화감독 숌
n=int(input()) # n번째 영화 입력
cnt=0 # 영화 시즌 카운터 변수
find_num=666 # 666 이 들어있는 숫자 중에 1번째 숫자 즉 시즌 1=666
while 1:
    if '666' in str(find_num): #숫자를 문자변환 후 비교
        cnt+=1
    if n==cnt: # 찾는 시즌 번호일치시
        print(find_num) #숫자 출력
        break
    find_num+=1 #아니면 1더해줌