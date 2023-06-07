def solution(k, m, score):
    answer = 0
    score = sorted(score)

    for i in range(len(score), m-1, -m):
        answer += score[i-m]*m # 정렬되어있으니까 마지막 값을 출력하면 해당 박스의 값이 됨

    return answer
print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

# 최대 이익을 산출하는 사과 박스
# 1-k의 등급을 정해진 사과
# m은 한박스에 들어가는 사과의 걋수
# 이익이 발생하지 않는 경우에는 0을 return한다.
# score에 사과 등급으로 배열 구성

# 최대이익을 산출하기 위해서는 뽑은 것들을 더했을 때 최대의 값을 산출할수 있어야한다. max사용?
# 뽑은 이후에는 삭제 pop을 사용한다...?

# if len(score) < m :
    # break

# max인것을 탐색한 후 위치를 출력하고 그 위치의 값을 삭제한다?
# 아니면 max값 출력하고 음... 그냥 삭제