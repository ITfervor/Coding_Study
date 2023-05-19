# 모의고사 (완전 탐색)
def solution(answers):
    test = {1:[1,2,3,4,5] ,2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    score = {1:0, 2:0, 3:0}
    for idx, answer in enumerate(answers):
        for key, value in test.items():
            if answer == value[idx % len(value)]:
                score[key] += 1

    highest = max(score.values())        
    result = [key for key,value in score.items() if value == highest]
    
    return result

print(solution([1,2,3,4,5]))