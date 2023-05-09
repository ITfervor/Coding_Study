# 정수 제곱근인지 판별해서 출력하는 문제
import math
def solution(n):
    x = math.sqrt(n)
    if x != int(x):
        return -1
    return math.pow(x+1, 2)
    