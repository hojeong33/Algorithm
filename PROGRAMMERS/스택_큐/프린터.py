def solution(priorities, location):
    answer = 0
    while len(priorities) != 0:
        MAX = max(priorities)
        temp = priorities.pop(0)
        if temp >= MAX:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(temp)
            if location:
                location -= 1
            else:
                location = len(priorities) - 1

    return answer
