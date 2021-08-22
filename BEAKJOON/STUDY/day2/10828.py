#스택
#출력해야되는 명령어 pop,size,empty,top
N=int(input())
stack=[]
for i in range(N):
    command=input()
    if 'push' in command:
        command=command[5:]
        stack.append(command)
    elif command=='pop' and stack:
        print(stack.pop())
    elif command=='size':
        print(len(stack))
    elif command=='empty' and stack:
        print(0)
    elif command=='empty' and len(stack)==0:
        print(1)
    elif command=='top'and stack:
        print(stack[-1])
    elif len(stack)==0:
        print(-1)
