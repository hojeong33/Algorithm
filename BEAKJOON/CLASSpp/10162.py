#전자레인지
T=int(input())
#A 300 B 60 C 10 --> 배수를 관계를 가진다.
A=T//300
a=T%300
B=a//60
b=a%60
C=b//10
c=b%10
if c==0:
    print('{} {} {}'.format(A,B,C))
else:
    print(-1)