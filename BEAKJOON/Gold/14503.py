#로봇 청소기
# 북동남서
dr=[-1,0,1,0]
dc=[0,1,-0,-1]

# 북->서 , 동->북, 남->동, 서-> 남

def find(r,c,d):
  global ans
  if miro[r][c]==0:
      miro[r][c]=2
      ans+=1
  for i in range(4): #왼쪽부터확인
      nd=(d+3)%4
      nr=r+dr[nd]
      nc=c+dc[nd]
      if miro[nr][nc]==0:
          find(nr,nc,nd)
          return
      d=nd
  nd=(d+2)%4 #후진
  nr=r+dr[nd]
  nc=c+dc[nd]
  if miro[nr][nc]==1:
      return
  find(nr,nc,d) #방향 유지

N,M=map(int,input().split())
r,c,d=map(int,input().split())
miro=[list(map(int,input().split())) for _ in range(N)]

ans=0
find(r,c,d)
print(ans)