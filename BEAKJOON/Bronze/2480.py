#주사위 세개
dices=list(map(int,input().split()))
dices.sort()
ans=0
if dices[0]==dices[2]:
    ans=10000+dices[0]*1000
elif dices[0]==dices[1] or dices[1]==dices[2]:
    ans=1000+dices[1]*100
else:
    ans=dices[2]*100

print(ans)