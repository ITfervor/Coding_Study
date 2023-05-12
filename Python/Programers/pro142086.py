def solution(s):
    answer = []
    a = 0
    b = 0
    for i in s:
        a = s.rfind(i,0,b)
        if (a != -1):
            answer.append(b-a)
        else:
            answer.append(a)
        b += 1
    return answer

print(solution("banana"))