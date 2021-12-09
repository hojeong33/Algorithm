def solution(N, number):
    check=[0,[N]]
    if N==number:
        answer=1
    for i in range(2,9):
        temp=set()
        temp.add(int(str(N)*i))
        for j in range(len(check[i-1])):
            temp.add((check[i-1][j]+N))
            temp.add((check[i-1][j]-N))
            temp.add((check[i-1][j]*N))
            temp.add((check[i-1][j]//N))
            temp.add((N-check[i-1][j]))
            if check[i-1][j]!=0:
                temp.add(N//check[i-1][j])
        temp=list(temp)
        check.append(temp)
    for i in range(1,len(check)):
       if number in check[i]:
           answer=i
           break
    else:
        answer=-1
    return answer




