#톱니바퀴
def turn(s,d):
    if d==1:
        w[s]=w[s][-1]+w[s][:7]
    else:
        w[s]=w[s][1:]+w[s][0]

w=[[]for _ in range(4)]
for i in range(4):
    w[i]=(input())
t=int(input())
for i in range(t):
    n,d=map(int,input().split())
    if n==1:
        if w[0][2]!=w[1][6]:
            turn(1,-d)
            if w[1][2-d]!=w[2][6]:
                turn(2,d)
                if w[2][2+d]!=w[3][6]:
                    turn(3,-d)
        turn(0,d)
    if n==2:
        if w[0][2]!=w[1][6]:
            turn(0,-d)
        if w[1][2]!=w[2][6]:
            turn(2,-d)
            if w[2][2-d]!=w[3][6]:
                turn(3,d)
        turn(1,d)
    if n==3:
        if w[1][2]!=w[2][6]:
            turn(1,-d)
            if w[0][2] != w[1][6-d]:
                turn(0, d)
        if w[2][2]!=w[3][6]:
            turn(3,-d)
        turn(2,d)
    if n==4:
        if w[2][2]!=w[3][6]:
            turn(2,-d)
            if w[1][2] != w[2][6-d]:
                turn(1, d)
                if w[0][2] != w[1][6+d]:
                    turn(0, -d)
        turn(3,d)
ans=0
for i in range(4):
    if w[i][0]=='1':
        if i==0:
            ans+=1
        elif i==1:
            ans+=2
        elif i==2:
            ans+=4
        else:
            ans+=8
print(ans)
