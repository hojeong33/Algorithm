def solution(people, limit):
    people.sort(reverse=True)
    cnt=0
    idx=1
    while len(people)>1:
        temp=people.pop(0)
        for i in range(len(people)):
            if temp+people[i]<=limit:
                people.pop(i)
                break
        cnt+=1
    if people:
        cnt+=1
    return cnt