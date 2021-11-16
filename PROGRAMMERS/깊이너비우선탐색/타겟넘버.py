def dfs():
    global answer
    global total
    global check
    while numbers:
        if check == len(numbers):
            if total == target:
                answer += 1
                total=0
        t = numbers.pop()
        for d in [1, -1]:
            t *= d
            total+=t
            check+=1
            print(total)
            # print(check)
            dfs()
            total-=t
            check-=1
    return answer

numbers=[1,1,1,1,1]
target=3
check=0
total=0
answer=0
print(dfs())


