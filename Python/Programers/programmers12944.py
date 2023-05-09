# 평균 구하기 값을 입력 받는다면 가능 한가?

# def solution(arr):
#     arr = []
#     a = list(map(int , input().split()))
#     arr.append(a)
#     s = 0
#     for i in range(arr.length + 1):
#         s += arr[i]
#     answer = s / arr.length
#     return answer


# 평균 값이 입력되어있는 상태로서 값을 구한다.

def solution(arr):
    if len(arr) == 0:
        return 0
    return sum(arr)/len(arr)