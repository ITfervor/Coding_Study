# def solution(numbers):
#     answer = []
#     add = 0
#     for i in range(0, len(numbers)):
#         if i == len(numbers):
#             break
#         add = numbers[i] + numbers[i+1]
#         answer.append(add) 
#         # set(answer)
#     return answer

def solution(numbers):
    answer = []
    add = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:
                add = numbers[i] + numbers[j]
            else:
                continue
            answer.append(add)
    answer = sorted(list(set(answer)))
    return answer


print(solution([2,1,3,4,1]))