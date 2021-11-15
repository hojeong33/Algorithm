from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    cnt=0
    # people=deque(people)
    while len(people)>1:
        temp=people.pop(0)
        for i in range(len(people)):
            if temp+people[i]<=limit:
                people.pop(i)
        cnt+=1
    if people:
        cnt+=1
    return cnt

print(solution([40,50,70,80],100))