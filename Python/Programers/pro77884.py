# 약수의 개수와 덧셈

def solution(left, right):
    list = []
    list1 = []
    answer = 0
    for i in range(left, right+1):
        for j in range(1,i+1):
            if i % j == 0 :
                list.append(j)
        if len(list) % 2 == 0:
            i = int(i)
            list1.append(i)
            list = []
        elif len(list) % 2 ==1:
            i = int(-i)
            list = []
    answer += list1[i]
    
    
    return answer

print(solution(13,17))

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
