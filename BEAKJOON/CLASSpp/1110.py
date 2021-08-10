#더하기 사이클
N=input()
if int(N)<10:
        origin='0'+N
else:
    origin=N
cnt=0
while 1:
    cnt += 1
    if int(N)<10:
        N='0'+N
    total=0
    for i in N:
        total+=int(i)
    total=str(total)
    ans=N[-1]+total[-1]
    if ans==origin:
        break
    N=ans

print(cnt)
