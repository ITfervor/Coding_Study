from itertools import combinations
def solution(number):
    cnt = 0
    numbers = list(combinations(number,3))
    for number1 in numbers:
        a = sum(number1)
        if a == 0:
            cnt += 1
    return cnt


a = [-2, 3, 0, 2, -5]
print(solution(a))