from math import *
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else: 
        answer = min(arr)
        arr.remove(answer)
        return arr

s = [4,3,2,1]
print(solution(s))